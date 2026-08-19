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

import ks3_rail_manifest as RAIL_MANIFEST

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


# ⊕ MRB-252, RULED 19 Aug 2026 — THE ONE COLOUR THAT IS NOT DESIGN'S, AND WHY
# THAT IS RECORDED HERE RATHER THAN WAIVED.
#
# Layer A exists to fail a colour that is in tokens.css and in none of Claude
# Design's frozen artifacts, because that colour is either invented or drifted
# and both are the same defect. `--ks3-ok-dark` is genuinely invented — Design
# never drew an on-dark green, which is precisely the gap MRB-252 was raised
# about and the reason the engine had been using a mark colour as body text at
# 2.89:1 for six instruments.
#
# So this is not an exemption list and it must never become one. Each entry
# carries the ticket that ruled it and the grounds it was measured against, and
# an entry only silences the "not in the reference" problem — it REPLACES it
# with a reported line, so a run of the gate still says out loud which colours
# do not trace to Design. Two further rules make it a gate rather than a hole:
#
#   · the VALUE is pinned here. Change #40DD84 in tokens.css and Layer A fails
#     naming both values, exactly as a drift would.
#   · a token listed here that no longer exists in tokens.css also fails. A
#     stale waiver outliving the thing it waived is how a list like this rots.
MINTED_TOKENS = {
    "--ks3-ok-dark": (
        "#40DD84",
        "MRB-252 comment 2 (Mide delegated; ruled 19 Aug 2026). Design drew no "
        "on-dark green, so `--ks3-ok` #12A150 was being used as body text at "
        "3.48:1 on --ks3-dark-panel and 2.89:1 on the #4A433C figures tile — "
        "against its own annotation. Same 146° hue, lifted. Measured 5.51:1 on "
        "the #4A433C tile (the binding ground), 6.63:1 on --ks3-dark-panel, "
        "7.03:1 on --ks3-dark-track, 9.37:1 on --ks3-ink."),
}


def check_provenance(repo_root="."):
    """Layer A. Returns (problems, checked_count).

    A colour that is not in any artifact is either invented or drifted. Both
    are exactly the failure this gate exists to prevent, so both fail — unless
    it is in MINTED_TOKENS, in which case it is REPORTED rather than passed.
    """
    blob = _artifact_text(repo_root)
    if not blob:
        return (["frozen reference artifacts missing from %s" % REF_DIR], 0)
    problems = []
    tokens = ks3_token_colours(repo_root)
    for name, hexval in sorted(tokens.items()):
        minted = MINTED_TOKENS.get(name)
        if minted and minted[0].lower() != hexval.lower():
            problems.append(
                "%s is minted at %s in ks3_parity.MINTED_TOKENS and tokens.css "
                "now says %s. A minted colour is a RULING with a measured "
                "value; moving it needs the ruling re-taken, not a token edit."
                % (name, minted[0], hexval))
            continue
        if minted:
            continue
        if hexval.lower() not in blob:
            problems.append(
                "%s = %s does not appear anywhere in Claude Design's frozen "
                "reference — invented or drifted" % (name, hexval))
    for name, (hexval, _why) in sorted(MINTED_TOKENS.items()):
        if name not in tokens:
            problems.append(
                "%s is listed in ks3_parity.MINTED_TOKENS and is not declared "
                "in tokens.css at all. Delete the entry with the token — a "
                "waiver that outlives what it waived is how this list rots."
                % name)
    # ⚠️ PRINTED, not returned. `verify_ks3.py` renders Layer A as one PASS
    # line with a colour count, and a minted colour that vanished into that
    # count would be a waiver nobody ever reads again. This is the one place
    # the run can say "these did not come from Design" out loud, so it does.
    for line in minted_report():
        print("     ⊕ minted, not from Design's reference: %s" % line)
    return (problems, len(tokens))


def minted_report():
    """The colours Layer A did NOT trace to Design, said out loud."""
    return ["%s = %s — %s" % (n, v, why)
            for n, (v, why) in sorted(MINTED_TOKENS.items())]


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

    # ⊕ MRB-250 — the parity rows that are REGISTERED AND NOT YET MEASURED,
    # counted and named. A skipped assertion must never be able to read as a
    # passed one, so the wait is reported on every build rather than being a
    # property of a list nobody prints.
    #
    # A page may be waited on only if it is a lesson slot the build knows about
    # and Design delivered — the slug has to be in `_B9_SLUGS`, which comes
    # from `docs/ks3/rail-manifest.md`, or in `_B10_SLUGS`, which comes from
    # `ks3_data/structure.py`. Anything else is a typo in a page
    # constant, and a typo would otherwise buy every row on it permanent
    # silence: the browser layer would skip it for ever and the count would
    # look like honest progress.
    waiting = _awaiting_pages(ks3_root)
    if waiting:
        rows = sum(1 for spec in COMPONENTS + CONTRAST
                   if spec["on"] in waiting)
        for rel in waiting:
            slug = os.path.basename(rel)[:-5]
            if slug not in _B9_SLUGS + _B10_SLUGS + _B11_SLUGS:
                problems.append(
                    "PARITY: %d row(s) are registered on /%s, which is neither "
                    "an authored lesson nor a slot this run is waiting on. A "
                    "page constant that names nothing is a row that can never "
                    "run and can never fail."
                    % (sum(1 for spec in COMPONENTS + CONTRAST
                           if spec["on"] == rel), rel))
        notes.append(
            "%d parity assertion(s) across %d page(s) are REGISTERED AND NOT "
            "YET MEASURED — the lesson records are still to be authored: %s. "
            "They begin measuring the moment each page renders its instrument; "
            "nothing has to be unparked."
            % (rows, len(waiting),
               ", ".join(os.path.basename(r)[:-5] for r in waiting)))

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
# ⊕ MRB-245 — the two live pages whose statement-panel cards shipped EMPTY.
# See `_rule_card` in build_ks3.py: six pills, two closing sentences and four
# problem cards were authored, drawn by Design, and rendered as blank `<li>`s.
B1_CELLS = "biology/cells-and-organisation/animal-and-plant-cells.html"
B1_SPEC = "biology/cells-and-organisation/specialised-cells.html"
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
# ⛔ DISCHARGED 18 Aug 2026 (MRB-248, Mide's diagram ruling). Kept in place and
# marked, per the build contract §12 reversal rule: the prediction in it came
# true and the record of that is worth more than the tidiness of deleting it.
#
# It said the first delivered unit to name a diagram slot would un-park these,
# and named B4 and B5 as the candidates. It was neither. B4 and B5 name twelve
# slots between them and every one is still `status: "needed"` — the second
# branch of `r_figure` wanted an asset under `ks3/figures/`, a directory that
# has never existed, so naming a slot could only ever produce a placeholder.
# What un-parked them is the ruling that code draws the diagram itself: b9-01
# and b9-03 now render a real `figure` block with a real drawing in it, so all
# three rows below are measured on b9-01 for the first time.
#
# The constant stays defined because it is what a future re-park would reach
# for, and because nothing should have to re-derive why these were ever parked.
_PARKED_NO_FIGURE = (
    "no lesson in the key stage renders a `figure` block — the C1 rebuild's "
    "six lessons carry `figures: []` and draw everything on canvas. Un-park "
    "with the first delivered unit that names a diagram slot (B4 and B5 both "
    "do).")
# ⊖ PARKED 18 Aug 2026 (MRB-248). The `moth-pair` drawer exists, is registered
# in `SVG_ART`, and is proved in a browser — but the FIGURE RECORD that would
# put it on b11-02 does not, because the drawer post-dates the b11-02 authoring
# pass. `r_figure` raises on a `status: "drawn"` figure whose `art` it cannot
# draw, deliberately, so authoring the record before the drawer existed would
# have failed the build for the other three authors as well; the author left
# `figures: []` and reported it, which was correct.
#
# ⚠️ UN-PARK BY DELETING THIS CONSTANT FROM THE FOUR ROWS, the moment b11-02's
# record names the figure. Nothing else changes: the rows are already written
# against the page and the selectors are already the ones the drawer emits.
_PARKED_NO_MOTH_FIGURE = (
    "b11-02 carries `figures: []` — the `moth-pair` drawer landed in the "
    "engine pass AFTER the lesson record was authored, and a `status: drawn` "
    "figure with no drawer fails the build by design. Un-park the moment the "
    "figure record is wired; the rows and selectors are already right.")
# ⊖ PARKED 18 Aug 2026 (MRB-248). `_rule_card`'s fourth part — what a method
# CANNOT do — exists in the engine and in the stylesheet, and no record authors
# `limit` yet: b11-04's author joined each limit to its own `body` with a
# single space, because the slot did not exist when they ran. Every byte is
# preserved; the paragraph break and the muted tone are not.
#
# ⚠️ UN-PARK BY DELETING THIS FROM THE ROW, the moment b11-04's `BANK_CARDS`
# move their second sentence into `limit`.
_PARKED_NO_LIMIT_SLOT = (
    "no record authors a statement-panel card's `limit` yet — b11-04's bank "
    "cards join it to `body` because the slot post-dates the authoring pass. "
    "Un-park when the strings move across.")
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

# ═══ BEGIN B4 ═══
B4_BAGS = "biology/breathing-and-gas-exchange/the-gas-exchange-system.html"
B4_JAR = "biology/breathing-and-gas-exchange/how-breathing-works.html"
B4_CROSS = "biology/breathing-and-gas-exchange/alveoli-built-for-exchange.html"
B4_FAULT = "biology/breathing-and-gas-exchange/exercise-asthma-and-smoking.html"
B4_LEAF = "biology/breathing-and-gas-exchange/stomata-and-gas-exchange-in-plants.html"
# ═══ END B4 ═══

# ═══ BEGIN B6 ═══
B6_DOSE = "biology/health-and-drugs/what-drugs-do-to-the-body.html"
B6_CLOCK = "biology/health-and-drugs/alcohol-and-smoking.html"
B6_CLAIMS = "biology/health-and-drugs/substance-misuse-and-decisions.html"
# ═══ END B6 ═══

# ═══ BEGIN B7 ═══
B7_BENCH  = "biology/photosynthesis/the-photosynthesis-reaction.html"
B7_TUNER  = "biology/photosynthesis/leaves-built-for-the-job.html"
B7_METHOD = "biology/photosynthesis/testing-a-leaf-for-starch.html"
B7_TRACE  = "biology/photosynthesis/why-almost-all-life-depends-on-it.html"
# ═══ END B7 ═══
# ═══ BEGIN B8 ═══
# ⊕ MRB-248. Five instruments, five pages, all five on ink.
B8_LEDGER = "biology/respiration/aerobic-respiration.html"
B8_DEMAND = "biology/respiration/why-every-cell-respires.html"
B8_DEBT   = "biology/respiration/anaerobic-respiration-in-humans.html"
B8_FERM   = "biology/respiration/fermentation.html"
B8_ROUTE  = "biology/respiration/aerobic-vs-anaerobic.html"
# ═══ END B8 ═══

# ═══ BEGIN B9 ═══
# ⊕ MRB-250. Six instruments, six pages, all six on ink.
#
# ⚠️ THESE PAGES DO NOT EXIST YET, AND REGISTERING AGAINST THEM NOW IS THE
# POINT. The B9 engine pass builds the six components; six separate authoring
# passes write the lesson records that render them. B8 shipped five instruments
# with twelve assertions between them because the rows were left until "after",
# and after never came — a green kinds gate over five unmeasured components.
# `_pages_needed` skips a page that has not been authored yet and
# `check_structure` reports the wait out loud, with a count and by name, so a
# row cannot sit unmeasured in silence. The moment an authoring pass lands the
# page, every row on it starts measuring — nothing to remember, nothing to
# edit, no flag to clear. See `_awaiting_pages`.
_B9_UNIT = "biology/ecosystems-and-interdependence/"
B9_CHAIN   = _B9_UNIT + "food-chains-and-food-webs.html"
B9_CYCLE   = _B9_UNIT + "predator-and-prey.html"
B9_REMOVE  = _B9_UNIT + "disturbing-a-food-web.html"
B9_SHELF   = _B9_UNIT + "pollinators-and-food-security.html"
B9_TOXIC   = _B9_UNIT + "toxic-build-up-in-a-food-chain.html"
B9_QUADRAT = _B9_UNIT + "sampling-an-ecosystem.html"

# The six slugs Design delivered, from `docs/ks3/rail-manifest.md`. A page path
# above that is NOT one of these, and does not exist in the built tree, is a
# TYPO rather than a page still being written — and a typo would otherwise buy
# permanent silence for every row on it. `check_structure` refuses one.
_B9_SLUGS = ("food-chains-and-food-webs", "predator-and-prey",
             "disturbing-a-food-web", "pollinators-and-food-security",
             "toxic-build-up-in-a-food-chain", "sampling-an-ecosystem")
# ═══ END B9 ═══


# ═══ BEGIN B10 ═══
# ⊕ MRB-248. The same shape as B9's block above and for the same reason: the
# engine pass registers these rows BEFORE the five authoring passes write the
# lesson records that render them. B8 shipped five instruments with twelve
# assertions between them because the rows were left until "after", and after
# never came. `_pages_needed` skips a page that has not been authored yet and
# `check_structure` reports the wait out loud, with a count and by name, so a
# row cannot sit unmeasured in silence. The moment an authoring pass lands the
# page, every row on it starts measuring — nothing to remember, nothing to
# edit, no flag to clear.
#
# ⚠️ THE SLUGS ARE `ks3_data/structure.py`'s, CHARACTER FOR CHARACTER. It is
# the law on what a page is called, and L3's is `how-we-worked-out-dna` while
# the lesson's title is "How we worked out DNA's structure" — a plausible
# `how-we-worked-out-dnas-structure` here would be a typo that buys every row
# on that page permanent silence, which is what `_B10_SLUGS` refuses.
_B10_UNIT = "biology/inheritance-and-dna/"
B10_PLOT    = _B10_UNIT + "variation-continuous-and-discontinuous.html"
B10_ZOOM    = _B10_UNIT + "chromosomes-genes-and-dna.html"
B10_MODEL   = _B10_UNIT + "how-we-worked-out-dna.html"
B10_CROSS   = _B10_UNIT + "passing-it-on-heredity.html"
B10_SPECIES = _B10_UNIT + "what-makes-a-species.html"

_B10_SLUGS = ("variation-continuous-and-discontinuous",
              "chromosomes-genes-and-dna", "how-we-worked-out-dna",
              "passing-it-on-heredity", "what-makes-a-species")
# ═══ END B10 ═══


# ═══ BEGIN B11 ═══
# ⊕ MRB-248. KS3 Biology's last unit: four instruments, four pages, all four on
# ink, plus one drawn figure.
#
# ⚠️ THESE PAGES DO NOT EXIST YET, AND REGISTERING AGAINST THEM NOW IS THE
# POINT — the same shape as B9's and B10's blocks above, and for the same
# reason. The engine pass builds the four components and the diagram; four
# separate authoring passes write the lesson records that render them. B8
# shipped five instruments with twelve assertions between them because the rows
# were left until "after", and after never came. `_pages_needed` skips a page
# that has not been authored yet and `check_structure` reports the wait out
# loud, with a count and by name, so a row cannot sit unmeasured in silence.
# The moment an authoring pass lands the page, every row on it starts
# measuring — nothing to remember, nothing to edit, no flag to clear.
#
# ⚠️ THE SLUGS ARE `ks3_data/structure.py`'s, CHARACTER FOR CHARACTER. A
# plausible mis-spelling here buys every row on that page permanent silence,
# which is what `_B11_SLUGS` refuses. L3's is
# `when-the-environment-changes-extinction` — no colon, no hyphen where the
# title has one.
_B11_UNIT = "biology/evolution-extinction-and-biodiversity/"
B11_ADV    = _B11_UNIT + "variation-and-competitive-success.html"
B11_SEL    = _B11_UNIT + "natural-selection.html"
B11_PRESS  = _B11_UNIT + "when-the-environment-changes-extinction.html"
B11_BLIGHT = _B11_UNIT + "biodiversity-and-gene-banks.html"

_B11_SLUGS = ("variation-and-competitive-success", "natural-selection",
              "when-the-environment-changes-extinction",
              "biodiversity-and-gene-banks")
# ═══ END B11 ═══


# ═══ BEGIN B5 ═══
B5_JOBS = "biology/reproduction/human-reproductive-systems.html"
B5_CMP = "biology/reproduction/gametes-and-fertilisation.html"
B5_DIAL = "biology/reproduction/the-menstrual-cycle.html"
B5_XBENCH = "biology/reproduction/gestation-placenta-and-birth.html"
B5_XPANEL = "biology/reproduction/lifestyle-and-the-developing-foetus.html"
B5_PARTS = "biology/reproduction/flowers-and-pollination.html"
B5_BECOMES = "biology/reproduction/fertilisation-seeds-and-fruit.html"
B5_SORT = "biology/reproduction/seed-dispersal.html"
# ═══ END B5 ═══

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
    # ⊕ MRB-245 — THE CARD PARTS THAT WERE AUTHORED AND NEVER DRAWN. Each of
    # these is registered against a page that actually renders it, and each
    # would have been "selector not present" for as long as the defect stood —
    # which is the point: a component the page does not draw fails HERE, and
    # ten empty `<li>`s did not fail anywhere.
    #
    # ⚖️ THE ROLE LINE'S TONE IS DATA, AND BOTH VALUES ARE MEASURED. b1-03
    # paints "In both · 4" muted and "Plant only · 3" accent, and the
    # difference IS the panel's claim — the plant's list is the animal's plus
    # three. One rule for both would erase the claim while looking correct.
    dict(name="a card's role line is mono accent-text", on=B1_SPEC,
         sel=".ks3-rule-role",
         props={"color": "#A93411", "font-family": "DM Mono",
                "font-size": "14px"}),
    dict(name="and it takes the MUTED tone where the record asks for it",
         on=B1_CELLS, sel='.ks3-rule-role[data-tone="muted"]',
         props={"color": "#5F564F", "font-family": "DM Mono"}),
    # A card with a role line above it makes its name the HEADLINE, not a
    # label — the three-part card Design draws on b1-04 and b7-01.
    dict(name="a three-part card's name is display 800, not the 18px label",
         on=B1_SPEC, sel=".ks3-rule-role + .ks3-rule-term",
         props={"font-family": "Bricolage Grotesque", "font-weight": "800",
                "font-size": "23px"}),
    dict(name="the card's examples line is muted mono at the foot",
         on=B1_SPEC, sel=".ks3-rule-eg",
         props={"color": "#5F564F", "font-family": "DM Mono",
                "font-size": "15px"}),
    # ⚖️ A PILL IS NOT A CONTROL. Ink outline, not `--ks3-option-border`: six
    # of these sit inside a card and none of them is pressable, and the option
    # border is what the key stage uses for something a student can tap.
    dict(name="a named-part pill is an ink outline on the inset, not a control",
         on=B1_CELLS, sel=".ks3-rule-chip",
         props={"background-color": "#F7EFE1", "border-top-color": "#221E1B",
                "border-top-width": "2px", "color": "#221E1B",
                "font-size": "17px"}),
    dict(name="the plant-only pills take the accent tint the record names",
         on=B1_CELLS,
         sel='.ks3-rule-chips[data-tone="accent-tint"] .ks3-rule-chip',
         props={"background-color": "#FCE7DE"}),
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
    # ⊕ MRB-257 · audit 3.19 — THIS ROW PINNED CREAM ON THE ACCENT, which is
    # 3.34:1 at 15px/800 against a token annotated "LARGE TEXT ONLY. Never body
    # size". Seven pages. The FILL is unchanged — the accent is what says
    # "chosen" — and only the letter moves, to ink, at 4.49:1. The contrast
    # pair in layer D moves with it, from a 3.0 mark bar to the 4.5 a letter
    # a student reads actually needs.
    dict(name="activity option CHOSEN badge", on=LESSON, drive="activity-chosen",
         sel='.ks3-check .ks3-option[aria-pressed="true"] .ks3-opt-mark',
         props={"background-color": "#E4572E", "color": "#221E1B"}),

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
    # ⊕ MRB-257 · audit 3.21 — 2.63:1, on all 18 pages measured, and no
    # opacity involved: this is an explicit pair, `--ks3-ink-ghost` on
    # `--ks3-band`. `--ks3-ink-faint` #6E655D is 4.75:1 and is still the
    # quietest thing on the row.
    dict(name="ladder option SPENT badge", on=LESSON, drive="ladder-answered",
         sel='.ks3-rung[data-mode="marked"] .ks3-option.is-spent .ks3-opt-mark',
         props={"background-color": "#F4E9D8", "color": "#6E655D"}),

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
    # ⊕ UN-PARKED 18 Aug 2026 and repointed at b9-01, the first page in the key
    # stage to render a `figure` block. `LESSON` (the rebuilt c1-04) authors
    # `figures: []`, so these three measured nothing there and said so.
    dict(name="figure frame", on=B9_CHAIN,
         sel=".ks3-figure",
         props={"margin-top": "28px"}),
    dict(name="figure caption", on=B9_CHAIN,
         sel=".ks3-figure figcaption",
         props={"font-size": "17px", "color": "#3B342E",
                "margin-top": "12px"}),
    # ⚠️ STILL PARKED, and for a different reason from the two above: the
    # pending slot is the `status: "needed"` placeholder, and no page that
    # renders a `figure` block is at that status. B9's two are `drawn`. The
    # fifteen slots still at `needed` are in B3, B4 and B5, which author no
    # `figure` BLOCK to render them through — so the placeholder is reachable
    # code with no page to measure it on. It un-parks the moment one of those
    # units adds the block, drawn or not.
    dict(name="figure pending slot", on=LESSON, parked=_PARKED_NO_FIGURE,
         sel=".ks3-figure-slot",
         props={"border-top-width": "3px", "border-top-style": "dashed",
                "border-top-color": "#C3B191"}),

    # ── the DRAWN figure (MRB-248, Mide's diagram ruling of 18 Aug 2026) ──
    #
    # Registered because the ruling requires it: "a diagram is a COMPONENT —
    # register it in §10 of the coverage manifest and give it parity rows, or
    # the gate cannot see it." Four rows, each pinning the property that makes
    # the drawing what it is rather than a property it shares with everything.
    #
    # The frame is asserted to be the SAME frame the `img` branch draws — 2px
    # ink, 24px radius — because a drawing and a photograph are one object on
    # the page and only one of them arrives as a file. If a later change gives
    # drawn figures their own frame, this row is what says so out loud.
    dict(name="drawn figure takes the photograph's frame", on=B9_CHAIN,
         sel=".ks3-figure-svg",
         props={"border-top-width": "2px", "border-top-color": "#221E1B",
                "border-top-left-radius": "24px"}),
    # ⚖️ The scroll region, and the row exists because losing it is invisible
    # on the machine anyone builds this on. Drop `overflow-x` and a desktop
    # browser shows no change at all; a phone shows a diagram at 47% with 7px
    # labels, or a page that scrolls sideways as a whole. Measured, so it
    # cannot be dropped quietly.
    dict(name="drawn figure scrolls rather than shrinking", on=B9_CHAIN,
         sel=".ks3-figure-scroll",
         props={"overflow-x": "auto"}),
    # The drawing carries its own ground rather than inheriting the block's. A
    # web drawn in ink needs the paper under it to be the paper.
    dict(name="drawn figure carries the page ground", on=B9_CHAIN,
         sel=".ks3-figure-svg",
         props={"background-color": "#FBF3E6"}),
    # ⚖️ THE ACCENT-TEXT ROW, and it is the one that matters most. A thread node
    # names an organism at 15px. `--ks3-accent` is 3.4:1 and may not carry text
    # that small; `--ks3-accent-text` is 6.0:1 and is the only orange allowed
    # under 24px. `_svg_text` raises on the wrong one at build time and this
    # measures the right one at render time, because a build-time check can only
    # see what it was asked to draw.
    dict(name="thread label is accent-TEXT, never accent", on=B9_CHAIN,
         sel=".ks3-figure-svg .ks3-web-thread-label",
         props={"fill": "#A93411"}),
    # ── the SECOND drawn figure: b10-03's base pairs (MRB-248) ──
    #
    # Registered on its own page rather than leaning on b9-01's rows, because
    # the two drawings assert different things and a shared row would pin
    # neither. What this pair pins is the drawing's ARGUMENT, not its decoration:
    # the constant-width guide is the reason the pairing rule exists, and the
    # size difference between a big base and a small one is what makes the
    # constant width true. Lose either and the figure still renders — as a
    # picture of an arbitrary rule, which is the version students already
    # memorise badly.
    dict(name="base-pair width guide is accent-TEXT", on=B10_MODEL,
         sel=".ks3-figure-svg text[style*='accent-text']",
         props={"fill": "#A93411"}),
    dict(name="the drawn figure frame holds on b10-03 too", on=B10_MODEL,
         sel=".ks3-figure-svg",
         props={"border-top-width": "2px", "border-top-color": "#221E1B",
                "background-color": "#FBF3E6"}),

    # The thread's third channel. Never-colour-alone means the numbered badge is
    # load-bearing, not decoration: it survives for a reader who cannot separate
    # the orange from the ink, and it carries the chain's ORDER, which no tint
    # could.
    dict(name="thread badge is a drawn ring, not a tint", on=B9_CHAIN,
         sel=".ks3-figure-svg circle",
         props={"stroke": "#E4572E", "stroke-width": "2px"}),

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
    # ⊕ MRB-221 — the `draft badge` layer-C pin is deleted with the badge. A
    # computed-style pin on a selector that matches nothing does not fail; it
    # measures nothing and reports PASS, which is the vacuous-gate failure mode
    # this file's own docstring warns about.
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
    # ⊕ MRB-242 — this row used to assert `display: grid`, which is what the
    # STYLESHEET did, not what Design draws: reference line 309 is a wrapping
    # flex row of pills. An assertion copied off the implementation cannot
    # catch the implementation drifting, and this one did not. Re-pointed at
    # the reference, and given the two properties that make a pill a pill.
    dict(name="fit-parts installs as a wrapping row of pills",
         on="biology/cells-and-organisation/animal-and-plant-cells.html",
         sel=".ks3-fit-parts",
         props={"display": "flex", "flex-wrap": "wrap"}),
    dict(name="a fit chip is a pill on the dark block, not a light option row",
         on="biology/cells-and-organisation/animal-and-plant-cells.html",
         sel=".ks3-fit-part",
         props={"border-top-left-radius": "999px", "min-height": "48px",
                "border-top-color": "#C6B9A7", "color": "#FBF3E6"}),
    dict(name="the fit job panel is the dark nested panel, not a cream inset",
         on="biology/cells-and-organisation/animal-and-plant-cells.html",
         sel=".ks3-fit-job", props={"background-color": "#3E3730"}),
    dict(name="the fit results card re-declares ink on its own cream ground",
         on="biology/cells-and-organisation/animal-and-plant-cells.html",
         sel=".ks3-fit-out",
         props={"background-color": "#FBF3E6", "color": "#221E1B"}),

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
    # ⊕ MRB-257 · audit 3.21 — the row's claim ("dims rather than
    # disappearing") was always right; .5 measured 3.11:1, which is nearer
    # disappearing than the claim allows. `--ks3-dim-spent` .65.
    dict(name="sorter SPENT option dims rather than disappearing",
         on=B2_SKEL, drive="jobsort-decided",
         sel='.ks3-jobsort-opt[disabled][aria-pressed="false"]',
         props={"opacity": "0.65"}),
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
    # ═══ BEGIN B4 ═══ rows
    #
    # Every value below is read out of `shared/tokens.css`, not estimated:
    #   --ks3-alert #FFC53D · --ks3-on-dark #FBF3E6 · --ks3-on-dark-muted #C6B9A7
    #   --ks3-on-dark-body #E7DECE · --ks3-dark-panel #3E3730 · --ks3-ink #221E1B
    #   --ks3-ink-muted #5F564F · --ks3-ink-body #3B342E · --ks3-ground #FBF3E6 · --ks3-ok #12A150
    #   --ks3-blue #2F5CE0 · --ks3-accent-text #A93411
    # Mutation-tested: each rule was deliberately broken in `shared/ks3.css` and
    # the row confirmed to fail before it was kept.
    #
    # ⚠️ FIVE OF THESE ROWS ARE ONE ROW, FIVE TIMES. Every B4 practical is
    # `ks3-block ks3-dark ks3-practical` and every one of the five instruments
    # inverts a panel to the CREAM ground inside that ink block. `.ks3-dark p`
    # is (0,1,1) and a bare instrument class is (0,1,0), so each of those five
    # panels loses unless its colour rule is scoped — and the failure is
    # #E7DECE on #FBF3E6, about 1.2:1: text that is present, correct, spelt
    # right and invisible. On B2 that defect could take one block. On B4 it
    # takes the whole unit in one pass, which is why all five are pinned
    # separately rather than one being taken as representative.

    # ── gas-compare (b4-01 #s-air) ──
    dict(name="the closing paragraph is ink on the cream panel",
         on=B4_BAGS, drive="gas-revealed", sel=".ks3-gas-close",
         props={"color": "#221E1B", "background-color": "#FBF3E6",
                "font-size": "19px"}),
    # ⚖️ ONE BAG, ONE COLOUR, IN THREE PLACES. The exhaled column is alert in
    # its heading, in its figure and in its bar, so a student can follow one
    # bag down the table; the inhaled column is the muted pair. Level the two
    # and the table becomes eight numbers rather than a comparison.
    dict(name="the exhaled figure is alert and the inhaled one is not",
         on=B4_BAGS, drive="gas-revealed",
         sel='.ks3-gas-cell[data-side="out"] .ks3-gas-num',
         props={"color": "#FFC53D", "font-family": "DM Mono"}),
    dict(name="the inhaled figure stays on-dark", on=B4_BAGS,
         drive="gas-revealed",
         sel='.ks3-gas-cell[data-side="in"] .ks3-gas-num',
         props={"color": "#FBF3E6"}),
    # ⚠️ REGISTERED AFTER THE FACT, and that is the point of the row. The cap
    # replaces the head row below 880px, and its colour rule lives inside the
    # media query — where it was (0,1,0), lost to `.ks3-dark p`, and rendered
    # `--ks3-on-dark-body` by accident at 8.77:1 while the authored
    # `--ks3-accent-text` was never applied. A rule that never applies cannot be
    # measured wrong, which is how it survived: had it won it would have been
    # #A93411 on `--ks3-dark-panel` at 1.78:1. This row pins the token that is
    # actually right for an ink ground and the specificity that lets it win.
    # The harness pins no viewport and headless lands under 820px, so the cap is
    # in its shown state here.
    dict(name="the narrow-screen cell caption takes the head row's own colour",
         on=B4_BAGS, drive="gas-revealed", sel=".ks3-gas-cap",
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "12px"}),
    # ⚖️ A CHOSEN PREDICTION IS ALERT AND NOTHING ELSE. R3: nothing marks while
    # the prediction is being made. If this row ever resolves to `--ks3-ok`
    # #12A150 an activity has started marking.
    dict(name="a chosen gas prediction is alert with ink text", on=B4_BAGS,
         sel='.ks3-gas-choice[aria-pressed="true"]',
         drive="gas-revealed",
         props={"background-color": "#FFC53D", "color": "#221E1B",
                "min-height": "44px"}),

    # ── bell-jar (b4-02 #s-model) ──
    #
    # ⚠️ THE ROW THAT MATTERS MOST IN THE UNIT. NOTES-B4 §3.2: *the chain is the
    # instrument, not the picture*. The chain sits on the cream ground inside
    # the ink block, so unscoped its four steps paint #E7DECE on #FBF3E6 — and
    # what is lost is not decoration, it is the ordered claim the whole lesson
    # and rung 1 are built on.
    dict(name="the chain steps are ink on the cream panel", on=B4_JAR,
         drive="bell-in", sel='.ks3-bell-chain[data-chain="in"] .ks3-bell-step',
         props={"color": "#221E1B", "font-size": "18px"}),
    dict(name="the chain panel is the page ground on an ink block", on=B4_JAR,
         drive="bell-in", sel=".ks3-bell-chainpanel",
         props={"background-color": "#FBF3E6"}),
    # ⚠️ THE LABEL, REGISTERED SEPARATELY FROM THE STEPS IT HEADS, because
    # registering the PANEL is what let it ship invisible. The steps and the
    # note were both rescued from `.ks3-dark p` and the label — a seventh `<p>`
    # in the same cream panel, taking a different colour from either — was not,
    # so `THE ORDER OF EVENTS` rendered at 1.21:1 above four perfectly legible
    # steps. It is visible from first paint in all three phases, so this row
    # needs no drive: if it is ever lost again the gate says so on load.
    dict(name="the chain label is the accent eyebrow, not on-dark body",
         on=B4_JAR, sel=".ks3-bell-chainlabel",
         props={"color": "#A93411", "font-family": "DM Mono",
                "font-size": "13px"}),
    # ⚖️ THE RESTING CHAIN IS THE ONLY MUTED ONE, because at rest it is not
    # describing anything happening. Level it with the other two and the block
    # opens looking as though a breath is under way.
    dict(name="the resting chain is muted, and only the resting one",
         on=B4_JAR, sel='.ks3-bell-chain[data-chain="rest"] .ks3-bell-step',
         props={"color": "#5F564F"}),
    dict(name="the pressure readout is mono on ink", on=B4_JAR,
         sel='.ks3-bell-read dd[data-read="pressure"]',
         props={"font-family": "DM Mono", "color": "#FBF3E6",
                "font-size": "18px"}),

    # ── crossing-counter (b4-03 #s-gradient) ──
    dict(name="the state note is ink on the cream panel", on=B4_CROSS,
         drive="cross-both-stopped", sel=".ks3-cross-note",
         props={"color": "#221E1B", "background-color": "#FBF3E6",
                "font-size": "18px"}),
    # ⚖️ THE OUTWARD BAR IS DRAWN, NOT DIMMED OUT OF EXISTENCE. Muted against
    # the inward bar's alert is a figure/ground distinction; if this row ever
    # resolves to the track colour or to `transparent`, the bar has become
    # invisible and the lesson has taught the one-way picture it exists to
    # remove. The `drive` puts both switches OFF first, which is the state a
    # student is most likely to read as "nothing is happening".
    dict(name="the outward bar is drawn in on-dark-muted, in every state",
         on=B4_CROSS, drive="cross-both-stopped",
         sel='.ks3-cross-fill[data-fill="out"]',
         props={"background-color": "#C6B9A7"}),
    dict(name="the inward bar is alert", on=B4_CROSS,
         drive="cross-both-stopped", sel='.ks3-cross-fill[data-fill="in"]',
         props={"background-color": "#FFC53D"}),
    # The NET tile is the only alert figure in the panel because it is the only
    # one that is a difference rather than a reading.
    dict(name="the net tile is the alert figure and the other two are not",
         on=B4_CROSS, sel='.ks3-cross-tile[data-tone="net"] .ks3-cross-tileval',
         props={"color": "#FFC53D", "font-family": "DM Mono",
                "font-size": "24px"}),
    dict(name="the alveolar tile stays on-dark", on=B4_CROSS,
         sel='.ks3-cross-tileval[data-tile="alveolar"]',
         props={"color": "#FBF3E6"}),

    # ── fault-bench (b4-04 #s-bench) ──
    #
    # The reveal is the largest run of cream-on-ink text in the unit: a
    # verdict, a headline and up to eight paragraphs across four rows.
    dict(name="the reveal headline is ink on the cream panel", on=B4_FAULT,
         drive="fault-opened", sel=".ks3-fault-answer",
         props={"color": "#221E1B", "font-family": "Bricolage Grotesque",
                "font-size": "25px"}),
    dict(name="the reveal rows read in ink body, not on-dark body",
         on=B4_FAULT, drive="fault-opened", sel=".ks3-fault-row dd",
         props={"color": "#3B342E", "font-size": "18px"}),
    dict(name="the reveal panel is the page ground on an ink block",
         on=B4_FAULT, drive="fault-opened", sel=".ks3-fault-reveal",
         props={"background-color": "#FBF3E6"}),
    # ⚖️ THE VERDICT IS NOT A MARK. It is the accent eyebrow whether the
    # student located the fault or not — never `--ks3-ok`, never `--ks3-danger`.
    # The reveal opens either way and this row is what keeps it that way.
    dict(name="the verdict is the accent eyebrow, not a marking colour",
         on=B4_FAULT, drive="fault-opened", sel=".ks3-fault-verdict",
         props={"color": "#A93411", "font-family": "DM Mono"}),

    # ── two-process-ledger (b4-05 #s-ledger) ──
    #
    # ⚖️ BLUE IS THE COMPENSATION POINT AND IS USED NOWHERE ELSE IN B4. It is
    # what makes a balanced reading read as a THIRD thing rather than as a weak
    # uptake — the flat line produced by two processes at full rate, which a
    # sensor cannot tell from a dead plant. The `drive` reaches it through the
    # slider, computing the balanced light from the instrument's own authored
    # constants, so this row also proves the branch is reachable in a browser.
    dict(name="the net bar is blue at the compensation point", on=B4_LEAF,
         drive="tpl-balanced", sel='.ks3-tpl-fill[data-tone="balanced"]',
         props={"background-color": "#2F5CE0"}),
    dict(name="the verdict panel is ink on cream at the compensation point",
         on=B4_LEAF, drive="tpl-balanced",
         sel='.ks3-tpl-verdict[data-verdict="balanced"] .ks3-tpl-vhead',
         props={"color": "#221E1B", "font-family": "Bricolage Grotesque"}),
    # ⚖️ THE RESPIRATION BAR IS MUTED, NOT GREEN, and it is never the
    # photosynthesis colour. The two bars being different colours is how a
    # student reads the top one as a constant and the second as the variable;
    # if this row ever resolves to #12A150 the ledger has two green bars and
    # the flat one stops looking like a different KIND of quantity.
    dict(name="the respiration bar is on-dark-muted, never the photo green",
         on=B4_LEAF, sel='.ks3-tpl-fill[data-fill="resp"]',
         props={"background-color": "#C6B9A7"}),
    dict(name="the photosynthesis bar is the ok green", on=B4_LEAF,
         drive="tpl-balanced", sel='.ks3-tpl-fill[data-fill="photo"]',
         props={"background-color": "#12A150"}),
    # ═══ END B4 ═══ rows
    # ═══ BEGIN B6 ═══ rows
    #
    # Every value below is read out of `shared/tokens.css`, not estimated:
    #   --ks3-alert #FFC53D · --ks3-on-dark #FBF3E6 · --ks3-on-dark-muted #C6B9A7
    #   --ks3-on-dark-body #E7DECE · --ks3-dark-panel #3E3730 · --ks3-ink #221E1B
    #   --ks3-ground #FBF3E6 · --ks3-accent-text #A93411
    # Mutation-tested: each rule was deliberately broken in `shared/ks3.css` and
    # the row confirmed to fail before it was kept.
    #
    # ⚠️ THE SAME ONE-RULE-THREE-TIMES HAZARD AS B4. All three B6 practicals are
    # `ks3-block ks3-dark ks3-practical`, so `.ks3-dark p` at (0,1,1) beats a
    # bare instrument class on all three pages at once, and each instrument has
    # a panel that inverts to the cream ground inside the ink block. Measured on
    # `.ks3-route-verdict` with the scope removed: #E7DECE on #FBF3E6, 1.21:1 —
    # the same number `.ks3-bell-chainlabel` shipped at. Each of the three is
    # pinned separately rather than one being taken as representative.

    # ── route-tracer (b6-01 #s-dose) ──
    #
    # ⚖️ THE VERDICT IS THE ONE SENTENCE THAT SAYS WHAT THE ROUTE WAS FOR
    # ("They were simply on the route."), and it is the unit's first
    # cream-inside-ink element. Pinned on colour AND ground, because either one
    # alone would pass with the panel painted the wrong way round.
    dict(name="the closing verdict is ink on the cream panel", on=B6_DOSE,
         drive="route-followed", sel=".ks3-route-verdict",
         props={"color": "#221E1B", "background-color": "#FBF3E6",
                "font-size": "18px"}),
    dict(name="the closing panel is the nested dark panel, not the page ground",
         on=B6_DOSE, drive="route-followed", sel=".ks3-route-else",
         props={"background-color": "#3E3730"}),
    # ⚖️ EXACTLY ONE ROW WEARS THE ALERT BORDER, and it is where the student
    # is. The stage list is the only picture in the unit (NOTES-B6 flag 14: no
    # figures anywhere, measured), so the border and the lit chip are doing the
    # work a diagram would do elsewhere.
    dict(name="the current stage is the alert-bordered row", on=B6_DOSE,
         drive="route-followed", sel='.ks3-route-step[data-state="current"]',
         props={"border-color": "#FFC53D", "border-width": "2px"}),
    dict(name="a reached stage chip is alert with ink text", on=B6_DOSE,
         drive="route-followed",
         sel='.ks3-route-step[data-state] .ks3-route-num',
         props={"background-color": "#FFC53D", "color": "#221E1B"}),
    # ⚖️ THE STAGE BODY IS BODY COPY ON INK AND MUST NOT BE THE HEADLINE
    # COLOUR: it is five paragraphs of reading, and #FBF3E6 at 18px over that
    # length is the glare Design's on-dark-body token exists to avoid.
    dict(name="the stage body reads in on-dark body", on=B6_DOSE,
         drive="route-followed", sel=".ks3-route-stepbody",
         props={"color": "#E7DECE", "font-size": "18px"}),
    # ⚖️ A RESTING STAGE IS MUTED, AND ONLY A RESTING ONE. Level it with the
    # reached rows and the block opens looking as though the dose has been
    # taken. No drive: at rest every row is resting, so this is measured on the
    # undriven load and a regression is reported before anything is clicked.
    dict(name="a resting stage title is muted, and only a resting one",
         on=B6_DOSE, sel='.ks3-route-step:not([data-state]) .ks3-route-steptitle',
         props={"color": "#C6B9A7"}),
    dict(name="the drug class is the alert mono line", on=B6_DOSE,
         sel=".ks3-route-class",
         props={"color": "#FFC53D", "font-family": "DM Mono",
                "font-size": "15px"}),
    # ⚖️ THE CHOSEN DRUG TAB IS ALERT AND NOTHING ELSE. R3: choosing a drug is
    # not answering anything, so if this row ever resolves to `--ks3-ok`
    # #12A150 the block has started marking a control that has no right answer.
    dict(name="the chosen drug tab is alert with ink text", on=B6_DOSE,
         sel='.ks3-route-tab[aria-pressed="true"]',
         props={"background-color": "#FFC53D", "color": "#221E1B",
                "min-height": "44px"}),

    # ── clearance-clock (b6-02 #s-clock) ──
    #
    # ⚖️ THE VERDICT IS WHERE THE BLOCK PAYS OFF — "which is exactly the number
    # of units. Every route you tried gave the same number of hours" — and it
    # is this instrument's cream-inside-ink element.
    dict(name="the clock verdict is ink on the cream panel", on=B6_CLOCK,
         drive="clock-run", sel=".ks3-clock-verdict",
         props={"color": "#221E1B", "background-color": "#FBF3E6",
                "font-size": "18px"}),
    # ⚖️ THE HOURS ARE THE ONLY ALERT FIGURE IN THE PANEL, because they are the
    # number that refuses to move. Level them with the units beside them and
    # the readout becomes two facts rather than one claim.
    dict(name="the hours-to-clear figure is the alert mono readout",
         on=B6_CLOCK, sel=".ks3-clock-hours",
         props={"color": "#FFC53D", "font-family": "DM Mono",
                "font-size": "16px"}),
    dict(name="the units drunk stay on-dark, not alert", on=B6_CLOCK,
         sel=".ks3-clock-units", props={"color": "#FBF3E6"}),
    # ⚠️ THE BLOOD BAR MUST BE DRAWN, and it must be the alert. If this ever
    # resolves to the track colour the bar has become invisible and the only
    # thing left saying anything is in the blood is a line of mono text.
    dict(name="the blood bar is alert on a lifted track", on=B6_CLOCK,
         sel=".ks3-clock-fill", props={"background-color": "#FFC53D"}),
    # ⚖️ THE FIX NOTE IS EXPLANATION, NOT VERDICT: it reads in on-dark body on
    # the lifted wash inside the dark panel, never in ink on cream. The two
    # surfaces are different claims and must not converge.
    dict(name="the fix note reads in on-dark body, not in ink", on=B6_CLOCK,
         sel=".ks3-clock-note", props={"color": "#E7DECE", "font-size": "18px"}),
    # ⚖️ A CHOSEN FIX IS ALERT AND NOTHING ELSE — never `--ks3-ok`, never
    # `--ks3-danger`. Picking "black coffee" is not a wrong answer; the bench
    # does not mark, and the note is what tells the student what it did.
    dict(name="the chosen fix is alert with ink text, and is not marked",
         on=B6_CLOCK, sel='.ks3-clock-fix[aria-pressed="true"]',
         props={"background-color": "#FFC53D", "color": "#221E1B",
                "min-height": "44px"}),
    # ⚖️ A DRINK NEVER LATCHES. Design draws every drink unpressed always: it
    # is an action, not a selection. If a drink ever resolves to the alert
    # ground it has become a choice the student appears to have made.
    dict(name="a drink control is never the chosen-state ground", on=B6_CLOCK,
         sel=".ks3-clock-drink",
         props={"background-color": "rgba(0, 0, 0, 0)", "color": "#FBF3E6",
                "min-height": "44px"}),

    # ── claim-check (b6-03 #s-claims) ──
    #
    # ⚠️ FOUR CREAM-INSIDE-INK ELEMENTS IN ONE PANEL — the largest count in the
    # unit, and exactly the shape of the B4 defect, where a panel was rescued
    # and a paragraph inside it was not. All four are pinned separately.
    dict(name="the claim reveal panel is the page ground on an ink block",
         on=B6_CLAIMS, drive="claims-checked", sel=".ks3-ccheck-verdict",
         props={"background-color": "#FBF3E6"}),
    # ⚖️ THE VERDICT WORD IS NOT A MARK. It is the accent eyebrow whether the
    # student named the fault or not — never `--ks3-ok` #12A150, never
    # `--ks3-danger` #FF6B6B. The reveal opens either way and this row is what
    # keeps it that way. The drive reaches it through a DELIBERATELY WRONG
    # pick, which is the state a marking colour would appear in first.
    dict(name="the verdict word is the accent eyebrow, not a marking colour",
         on=B6_CLAIMS, drive="claims-checked", sel=".ks3-ccheck-word",
         props={"color": "#A93411", "font-family": "DM Mono",
                "font-size": "14px"}),
    dict(name="the named fault is ink display type on the cream panel",
         on=B6_CLAIMS, drive="claims-checked", sel=".ks3-ccheck-answer",
         props={"color": "#221E1B", "font-family": "Bricolage Grotesque",
                "font-size": "22px"}),
    dict(name="the reveal reasoning reads in ink body, not on-dark body",
         on=B6_CLAIMS, drive="claims-checked", sel=".ks3-ccheck-why",
         props={"color": "#3B342E", "font-size": "18px"}),
    dict(name="the what-would-settle-it line reads in ink body", on=B6_CLAIMS,
         drive="claims-checked", sel=".ks3-ccheck-settle",
         props={"color": "#3B342E", "font-size": "18px"}),
    # ⚖️ R10, PINNED AS A COLOUR. A chosen fault takes the alert border and
    # the alert letter, and its LABEL COLOUR DOES NOT MOVE — because a chosen
    # option is not a right one. If either of these two rows ever resolves to
    # `--ks3-ok` or `--ks3-danger`, the bench has started marking and the house
    # rule Design states on the page has been lost.
    dict(name="a chosen fault is alert-bordered and its label does not move",
         on=B6_CLAIMS, drive="claims-checked",
         sel='.ks3-ccheck-fault[aria-pressed="true"]',
         props={"border-color": "#FFC53D", "color": "#FBF3E6",
                "min-height": "44px"}),
    dict(name="the chosen fault's letter is alert, and is not a tick",
         on=B6_CLAIMS, drive="claims-checked",
         sel='.ks3-ccheck-fault[aria-pressed="true"] .ks3-ccheck-mark',
         props={"color": "#FFC53D", "border-color": "#FFC53D"}),
    # ⚖️ THE FAULTS THAT WERE NOT PICKED DIM; THEY ARE NOT STRUCK THROUGH AND
    # THEY ARE NOT RECOLOURED. Every one of them is a TRUE statement about
    # evidence — the pool is one-to-one — so nothing here may present them as
    # wrong answers.
    # ⊕ MRB-257 · audit 3.8 — 0.5 PUT THE FEEDBACK AT 3.96:1 AND ITS LETTER AT
    # 2.70:1, and this is the state where a student reads what was wrong.
    # `--ks3-dim-spent` is .65. The letter needed a second change as well — at
    # .65 `--ks3-on-dark-muted` would still only reach ~3.5 — so it takes
    # `--ks3-on-dark` in this state, and the row below is what holds that.
    dict(name="an unpicked fault dims and stays on-dark", on=B6_CLAIMS,
         drive="claims-checked",
         sel='.ks3-ccheck-fault[disabled][aria-pressed="false"]',
         props={"opacity": "0.65", "color": "#FBF3E6"}),
    dict(name="a spent fault's letter goes on-dark so the dim cannot bury it",
         on=B6_CLAIMS, drive="claims-checked",
         sel='.ks3-ccheck-fault[disabled][aria-pressed="false"] .ks3-ccheck-mark',
         props={"color": "#FBF3E6"}),
    dict(name="the claim itself is display type on ink", on=B6_CLAIMS,
         sel=".ks3-ccheck-claim",
         props={"color": "#FBF3E6", "font-family": "Bricolage Grotesque",
                "font-size": "26px"}),
    # ═══ END B6 ═══ rows

    # ═══ BEGIN B5 ═══ rows
    #
    # Every value below is read out of `shared/tokens.css`, not estimated:
    #   --ks3-alert #FFC53D · --ks3-on-dark #FBF3E6 · --ks3-on-dark-muted #C6B9A7
    #   --ks3-on-dark-body #E7DECE · --ks3-dark-panel #3E3730 · --ks3-ink #221E1B
    #   --ks3-ink-muted #5F564F · --ks3-ground #FBF3E6 · --ks3-accent #E4572E
    #   --ks3-accent-text #A93411 · --ks3-band #F4E9D8
    # Mutation-tested: each rule was deliberately broken in `shared/ks3.css`
    # (the SOURCE — `verify_ks3.py` rebuilds before measuring and would
    # overwrite a mutation applied to the built tree) and the row confirmed to
    # fail before it was kept.
    #
    # ⚠️ THE SAME ONE-RULE-EIGHT-TIMES HAZARD AS B4 AND B6, AND HERE IT IS THE
    # WHOLE UNIT. All eight B5 practicals are `ks3-block ks3-dark
    # ks3-practical`, so `.ks3-dark p` at (0,1,1) beats a bare instrument class
    # on eight pages at once. Five of them draw a panel that inverts to the
    # CREAM ground inside the ink block — and it is the same component five
    # times, which is why the cream rows below are measured on more than one
    # page rather than one being taken as representative: a per-page override
    # is exactly what "keep them identical" (NOTES-B5 §6) forbids, and only
    # measuring twice can see it.

    # ── the commit family · the cream reveal (b5-01 / b5-05 / b5-08) ──
    #
    # ⚖️ PINNED ON COLOUR AND BACKGROUND TOGETHER. Either alone passes with the
    # panel painted the wrong way round — cream text on the ink panel measures
    # a healthy contrast and is the wrong component.
    dict(name="the reveal panel is the page ground on an ink block",
         on=B5_JOBS, drive="b5-item-checked", sel=".ks3-b5c-reveal",
         props={"background-color": "#FBF3E6"}),
    # ⚖️ THE VERDICT WORD IS NOT A MARK (MRB-196 R10). It is the accent eyebrow
    # whether the student had it or not — never `--ks3-ok` #12A150, never
    # `--ks3-danger` #FF6B6B — because the reveal opens either way and names
    # the right answer in full. The drive reaches it through a DELIBERATELY
    # WRONG pick, which is the state a marking colour would appear in first.
    dict(name="the verdict word is the accent eyebrow, not a marking colour",
         on=B5_JOBS, drive="b5-item-checked", sel=".ks3-b5c-word",
         props={"color": "#A93411", "font-family": "DM Mono",
                "font-size": "14px"}),
    dict(name="the answer line is ink display type on the cream panel",
         on=B5_JOBS, drive="b5-item-checked", sel=".ks3-b5c-answer",
         props={"color": "#221E1B", "font-family": "Bricolage Grotesque",
                "font-size": "23px"}),
    dict(name="the reveal reasoning reads in ink, not on-dark body",
         on=B5_JOBS, drive="b5-item-checked", sel=".ks3-b5c-why",
         props={"color": "#221E1B", "font-size": "18px"}),
    # ⚖️ THE SAME COMPONENT, MEASURED AGAIN ON A SECOND PAGE. NOTES-B5 §6
    # requires b5-04's bench and b5-05's to stay identical, and this is the
    # only assertion that can see them diverge.
    dict(name="the twin bench's reveal is the same cream panel, not a copy",
         on=B5_XPANEL, drive="b5-item-checked", sel=".ks3-b5c-reveal",
         props={"background-color": "#FBF3E6"}),
    dict(name="the twin bench's reasoning is the same ink, not a copy",
         on=B5_XPANEL, drive="b5-item-checked", sel=".ks3-b5c-why",
         props={"color": "#221E1B", "font-size": "18px"}),
    # ⚖️ AND THE OTHER HALF OF THE TWIN, on b5-04 itself. Measuring b5-05 alone
    # would pass a b5-04 that had been given a treatment of its own — which is
    # precisely what NOTES-B5 §6 forbids, and the direction the drift would
    # most plausibly go, because b5-04's bench was authored by a different pass.
    dict(name="b5-04's bench is the same component, measured on its own page",
         on=B5_XBENCH, drive="b5-item-checked", sel=".ks3-b5c-reveal",
         props={"background-color": "#FBF3E6"}),
    dict(name="and its verdict word is the same accent eyebrow", on=B5_XBENCH,
         drive="b5-item-checked", sel=".ks3-b5c-word",
         props={"color": "#A93411", "font-family": "DM Mono",
                "font-size": "14px"}),
    dict(name="and its substance line is the same alert mono", on=B5_XBENCH,
         sel=".ks3-b5c-meta",
         props={"color": "#FFC53D", "font-family": "DM Mono",
                "font-size": "15px"}),
    # ⚖️ THE BIJECTION BLOCK'S OPTIONS ARE JOB SENTENCES, and they are on the
    # dark panel rather than the page ground — b5-06 is the one commit bench
    # whose options are long enough for the wrong ground to be unreadable
    # rather than merely wrong.
    dict(name="an option on the flower bench sits on the dark panel",
         on=B5_PARTS, sel=".ks3-b5c-opt",
         props={"background-color": "#3E3730", "color": "#FBF3E6",
                "min-height": "44px"}),
    dict(name="a chosen option is alert-bordered and its label does not move",
         on=B5_PARTS, drive="b5-item-checked",
         sel='.ks3-b5c-opt[aria-pressed="true"]',
         props={"border-color": "#FFC53D", "color": "#FBF3E6"}),

    # ── b5-05's week window, inside that cream panel ──
    #
    # ⚠️ FOUR MORE CREAM-INSIDE-INK ELEMENTS IN ONE PANEL — exactly the shape
    # of the B4 defect, where a panel was rescued and a paragraph inside it was
    # not. Each is pinned separately, because a rule on the panel is not a rule
    # on its children.
    dict(name="the window caption is ink-muted mono on the cream panel",
         on=B5_XPANEL, drive="b5-item-checked", sel=".ks3-b5c-winlabel",
         props={"color": "#5F564F", "font-family": "DM Mono",
                "font-size": "12px"}),
    dict(name="the window sentence reads in ink, not on-dark body",
         on=B5_XPANEL, drive="b5-item-checked", sel=".ks3-b5c-wintext",
         props={"color": "#221E1B", "font-size": "17px"}),
    dict(name="the week ticks are ink-muted mono, not invisible",
         on=B5_XPANEL, drive="b5-item-checked", sel=".ks3-b5c-winticks span",
         props={"color": "#5F564F", "font-family": "DM Mono"}),
    # ⚠️ THE WINDOW BAR MUST BE DRAWN, and on the band rather than on the cream
    # it sits on. If the fill ever resolves to the track colour the window has
    # become an empty rectangle and the only thing left saying when an exposure
    # matters is a line of prose.
    dict(name="the window fill is the accent on a band track", on=B5_XPANEL,
         drive="b5-item-checked", sel=".ks3-b5c-winfill",
         props={"background-color": "#E4572E"}),
    dict(name="the window track is the band, not the cream it sits on",
         on=B5_XPANEL, drive="b5-item-checked", sel=".ks3-b5c-wintrack",
         props={"background-color": "#F4E9D8"}),

    # ── b5-08's deciding-feature line, inside that cream panel ──
    #
    # ⚖️ THE OBSERVABLE THAT SETTLES IT IS THE THING BEING TAUGHT (NOTES-B5
    # §2.6), which is why it is a line of its own rather than a clause inside
    # the why — and why it is pinned rather than left to the panel's rule.
    dict(name="the deciding feature is ink-muted mono on the cream panel",
         on=B5_SORT, drive="b5-item-checked", sel=".ks3-b5c-tell",
         props={"color": "#5F564F", "font-family": "DM Mono",
                "font-size": "15px"}),
    dict(name="its caption is a block, not a run-on with the feature",
         on=B5_SORT, drive="b5-item-checked", sel=".ks3-b5c-telllabel",
         props={"color": "#5F564F", "display": "block"}),

    # ── the commit family · the ink chrome, measured at rest ──
    #
    # No drive: at rest every one of these is in its resting state, so a
    # regression is reported before anything is clicked.
    dict(name="the item name is display type on the nested dark panel",
         on=B5_JOBS, sel=".ks3-b5c-name",
         props={"color": "#FBF3E6", "font-family": "Bricolage Grotesque",
                "font-size": "26px"}),
    dict(name="the item's system line is the alert mono line", on=B5_JOBS,
         sel=".ks3-b5c-meta",
         props={"color": "#FFC53D", "font-family": "DM Mono",
                "font-size": "15px"}),
    dict(name="the bench panel is the nested dark panel, not the page ground",
         on=B5_PARTS, sel=".ks3-b5c-panel",
         props={"background-color": "#3E3730"}),
    # ⚖️ THE SPECIMEN DESCRIPTION IS THE EVIDENCE THE SORT IS MADE ON, and it
    # is body copy on ink at 18px — not the headline colour, which over that
    # length is the glare `--ks3-on-dark-body` exists to avoid.
    dict(name="the specimen description reads in on-dark body", on=B5_SORT,
         sel=".ks3-b5c-context",
         props={"color": "#E7DECE", "font-size": "18px"}),
    dict(name="the mono ask above the options is muted, not headline",
         on=B5_SORT, sel=".ks3-b5c-ask",
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "14px"}),
    # ⚖️ A CHOSEN TAB IS ALERT AND NOTHING ELSE (R10). Choosing which structure
    # to look at is not answering anything, so if this row ever resolves to
    # `--ks3-ok` #12A150 the bench has started marking a control that has no
    # right answer.
    dict(name="the chosen tab is alert with dark-panel text", on=B5_JOBS,
         sel='.ks3-b5c-tab[aria-pressed="true"]',
         props={"background-color": "#FFC53D", "color": "#3E3730",
                "min-height": "44px"}),
    dict(name="an unchosen tab is transparent and stays on-dark body",
         on=B5_JOBS, sel='.ks3-b5c-tab[aria-pressed="false"]',
         props={"background-color": "rgba(0, 0, 0, 0)", "color": "#E7DECE",
                "min-height": "44px"}),
    # ⊕ THE CORRECTION, PINNED. `.ks3-reveal-btn` is ink on an ink border, and
    # this block's ground IS `--ks3-ink` — so the shipped rule paints an
    # invisible control. If this row ever resolves to #221E1B the check button
    # has disappeared into the block and the instrument cannot be operated.
    dict(name="the check button is inverted on ink, not ink on ink",
         on=B5_JOBS, sel=".ks3-b5c-check",
         props={"background-color": "#FBF3E6", "color": "#221E1B",
                "min-height": "44px"}),
    dict(name="the hint beside it is muted mono", on=B5_JOBS,
         sel=".ks3-b5c-hint",
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "15px"}),

    # ── the comparison rows (b5-02 #s-compare · b5-07 #s-becomes) ──
    #
    # ⚖️ THE LEAD COLUMN IS NOT ALWAYS THE FIRST, and these four rows are what
    # prove it. Design paints the column the lesson is ABOUT in the alert: the
    # sperm on b5-02, and what each part turns into on b5-07. Measuring one
    # page would pass an implementation that hard-codes the first data column
    # and puts b5-07's emphasis on the flower that no longer exists.
    dict(name="the lead column is the alert one", on=B5_CMP,
         sel=".ks3-cmp-row .ks3-cmp-cell[data-lead] .ks3-cmp-val",
         props={"color": "#FFC53D", "font-size": "17px"}),
    dict(name="the other column stays on-dark body", on=B5_CMP,
         sel=".ks3-cmp-row .ks3-cmp-cell:not([data-lead]) .ks3-cmp-val",
         props={"color": "#E7DECE", "font-size": "17px"}),
    dict(name="on the mirrored table the lead is the SECOND column",
         on=B5_BECOMES,
         sel=".ks3-cmp-row .ks3-cmp-cell:not([data-lead]) .ks3-cmp-val",
         props={"color": "#E7DECE"}),
    dict(name="and its alert column is the after-fertilisation one",
         on=B5_BECOMES, sel=".ks3-cmp-row .ks3-cmp-cell[data-lead] .ks3-cmp-val",
         props={"color": "#FFC53D"}),
    # ⚖️ THE WHOLE ROW IS THE BUTTON (NOTES-B5 §2.5) — no separate chevron
    # control. A block-level control at the row's full width is the difference
    # between a 700px tap target and a 44px one, and it is drawn that way on
    # both pages.
    dict(name="the whole row is the button, at the row's full width",
         on=B5_CMP, sel=".ks3-cmp-btn",
         props={"display": "block", "min-height": "44px",
                "background-color": "rgba(0, 0, 0, 0)"}),
    dict(name="the row's name column is on-dark, not body", on=B5_CMP,
         sel=".ks3-cmp-row .ks3-cmp-name",
         props={"color": "#FBF3E6", "font-size": "17px"}),
    dict(name="the table sits on the nested dark panel", on=B5_CMP,
         sel=".ks3-cmp-table", props={"background-color": "#3E3730"}),
    # ⚖️ THE WHY IS THE REASON THE ROW EXISTS, and it is on the ink table
    # rather than on a cream panel — a different surface from the commit
    # family's reveal, and the two must not converge.
    dict(name="an opened row's why reads in on-dark body on ink", on=B5_CMP,
         drive="b5-rows-opened", sel=".ks3-cmp-why",
         props={"color": "#E7DECE", "font-size": "18px"}),
    dict(name="its Why: label lifts to on-dark display type", on=B5_CMP,
         drive="b5-rows-opened", sel=".ks3-cmp-whylabel",
         props={"color": "#FBF3E6", "font-family": "Bricolage Grotesque"}),
    # ⚖️ AN OPEN ROW IS TINTED, NOT MARKED. Every row's why is true, so opening
    # one is not answering anything: this is the accent's own wash and never
    # `--ks3-ok` or `--ks3-danger`.
    dict(name="an open row takes the accent wash, not a marking colour",
         on=B5_CMP, drive="b5-rows-opened", sel=".ks3-cmp-row[data-open]",
         props={"background-color": "rgba(228, 87, 46, 0.1)"}),
    # ⚠️ THE SCALE BARS MUST BE DRAWN. If either resolves to the track colour
    # the "to scale" block has become two empty pills and the note under it —
    # where the eight-thousandfold figure lives — is talking about nothing.
    dict(name="the smaller scale bar is the alert one", on=B5_CMP,
         sel=".ks3-cmp-scalebar[data-lead]",
         props={"background-color": "#FFC53D"}),
    dict(name="the reference scale bar is muted, not the alert", on=B5_CMP,
         sel=".ks3-cmp-scalebar:not([data-lead])",
         props={"background-color": "#C6B9A7"}),

    # ── cycle-dial (b5-03 #s-dial) ──
    #
    # ⚖️ THE RELEASE MARKER IS THE INSTRUMENT. Everything else on this bench is
    # scaffolding for one observation — change the length and the alert line
    # moves. If this row ever resolves to the track colour the release day has
    # become invisible and the block is a slider with two paragraphs under it.
    dict(name="the release marker is the one alert line on the track",
         on=B5_DIAL, sel=".ks3-dial-release",
         props={"background-color": "#FFC53D"}),
    # ⚖️ AND THE BLEEDING BAND IS NOT ALSO ALERT. Two alert regions on one 46px
    # track and the eye cannot tell which one is being asked about.
    dict(name="the bleeding band is the accent wash, not a second alert",
         on=B5_DIAL, sel=".ks3-dial-shed",
         props={"background-color": "rgba(228, 87, 46, 0.3)"}),
    dict(name="the day marker is on-dark against both of them", on=B5_DIAL,
         sel=".ks3-dial-marker", props={"background-color": "#FBF3E6"}),
    dict(name="the day readout is display type on ink", on=B5_DIAL,
         sel=".ks3-dial-day",
         props={"color": "#FBF3E6", "font-family": "Bricolage Grotesque",
                "font-size": "30px"}),
    dict(name="the phase name is the alert mono line", on=B5_DIAL,
         sel=".ks3-dial-phase",
         props={"color": "#FFC53D", "font-family": "DM Mono",
                "font-size": "15px"}),
    # ⚖️ BOTH ORGAN PANELS ARE ON SCREEN AT EVERY DAY, and they read in body
    # copy rather than the headline colour: they are two paragraphs the student
    # re-reads at each day, and #FBF3E6 at 18px over that length is the glare
    # `--ks3-on-dark-body` exists to avoid.
    dict(name="the two organ panels read in on-dark body", on=B5_DIAL,
         sel=".ks3-dial-celltext",
         props={"color": "#E7DECE", "font-size": "18px"}),
    dict(name="the organ captions are muted mono", on=B5_DIAL,
         sel=".ks3-dial-celllabel",
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "12px"}),
    dict(name="a chosen cycle length is alert, and is not marked", on=B5_DIAL,
         sel='.ks3-dial-len[aria-pressed="true"]',
         props={"background-color": "#FFC53D", "color": "#3E3730",
                "min-height": "44px"}),
    # ⚖️ THE STEP BUTTONS ARE A 44px TAP TARGET. They exist for keyboard and
    # for a phone, where a 12px slider thumb is not operable — so their size is
    # the assertion, not their colour.
    dict(name="the day step buttons are full tap targets", on=B5_DIAL,
         sel=".ks3-dial-step",
         props={"width": "44px", "height": "44px", "color": "#FBF3E6"}),
    dict(name="the note under the panel is muted, not body", on=B5_DIAL,
         sel=".ks3-dial-note",
         props={"color": "#C6B9A7", "font-size": "18px"}),
    # ⚖️ MEASURED AGAIN AFTER THE LENGTH HAS BEEN CHANGED, which is the state
    # the whole instrument exists to produce. A release marker that is drawn
    # correctly at rest and repainted on relengthening would pass every row
    # above and still lose the lesson.
    dict(name="the release marker survives a change of cycle length",
         on=B5_DIAL, drive="b5-dial-relengthed", sel=".ks3-dial-release",
         props={"background-color": "#FFC53D"}),
    dict(name="and the note is still readable once a length has been tried",
         on=B5_DIAL, drive="b5-dial-relengthed", sel=".ks3-dial-note",
         props={"color": "#C6B9A7", "font-size": "18px"}),
    # ═══ END B5 ═══ rows

    # ═══ BEGIN B7 ═══ rows
    #
    # Every value below is read out of `shared/tokens.css`, not estimated:
    #   --ks3-alert #FFC53D · --ks3-on-dark #FBF3E6 · --ks3-on-dark-muted #C6B9A7
    #   --ks3-on-dark-body #E7DECE · --ks3-dark-panel #3E3730 · --ks3-ink #221E1B
    #   --ks3-ink-muted #5F564F · --ks3-ground #FBF3E6 · --ks3-accent #E4572E
    #   --ks3-accent-text #A93411 · --ks3-card #FFFCF5 · --ks3-ok #12A150
    # Mutation-tested: each rule was deliberately broken in `shared/ks3.css`
    # (the SOURCE — `verify_ks3.py` rebuilds before measuring and would
    # overwrite a mutation applied to the built tree) and the row confirmed to
    # fail before it was kept.
    #
    # ⚠️ THE SAME ONE-RULE-FOUR-TIMES HAZARD AS B4, B5 AND B6, AND HERE IT IS
    # AGAIN THE WHOLE UNIT. All four B7 practicals are `ks3-block ks3-dark
    # ks3-practical`, so `.ks3-dark p` at (0,1,1) beats a bare instrument class
    # on four pages at once. All four draw a panel that inverts to the CREAM
    # ground inside the ink block, and the elements INSIDE those panels are
    # pinned one at a time — because a rule on the panel is not a rule on its
    # children, which is exactly how `.ks3-bell-chainlabel` shipped at 1.21:1
    # inside a panel that had already been rescued.

    # ── b7-01 · reactant-remover, the cream verdict inside the ink bench ──
    #
    # ⚖️ PINNED ON COLOUR AND BACKGROUND TOGETHER. Either alone passes with the
    # panel painted the wrong way round — cream text on the ink panel measures
    # a healthy contrast and is the wrong component.
    dict(name="the iodine verdict is the page ground on an ink block",
         on=B7_BENCH, drive="b7-leaf-tested", sel=".ks3-rr-verdict",
         props={"background-color": "#FBF3E6"}),
    # ⚖️ THE IODINE TAG IS NOT A MARK (MRB-196 R10). It is the accent eyebrow
    # on every one of the seven branches — never `--ks3-ok` #12A150, never
    # `--ks3-danger` #FF6B6B — because the bench shows a CONSEQUENCE and never
    # a verdict on the student. The drive reaches it through a REMOVAL, which
    # is the state a marking colour would appear in first.
    dict(name="the iodine tag is the accent eyebrow, not a marking colour",
         on=B7_BENCH, drive="b7-leaf-tested", sel=".ks3-rr-tag",
         props={"color": "#A93411", "font-family": "DM Mono",
                "font-size": "14px"}),
    dict(name="the starch headline is ink display type on the cream panel",
         on=B7_BENCH, drive="b7-leaf-tested", sel=".ks3-rr-head",
         props={"color": "#221E1B", "font-family": "Bricolage Grotesque",
                "font-size": "23px"}),
    dict(name="the iodine reasoning reads in ink, not on-dark body",
         on=B7_BENCH, drive="b7-leaf-tested", sel=".ks3-rr-why",
         props={"color": "#221E1B", "font-size": "18px"}),
    # ── b7-01 · the ink chrome, measured at rest ──
    #
    # No drive: at rest every one of these is in its resting state, so a
    # regression is reported before anything is clicked.
    dict(name="the setup line is on-dark, not swallowed by the panel",
         on=B7_BENCH, sel=".ks3-rr-setup",
         props={"color": "#FBF3E6", "font-size": "20px"}),
    dict(name="the rate readout is the alert mono line", on=B7_BENCH,
         sel=".ks3-rr-rate",
         props={"color": "#FFC53D", "font-family": "DM Mono",
                "font-size": "16px"}),
    dict(name="a dial's name is muted mono on ink", on=B7_BENCH,
         sel=".ks3-rr-dialname",
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "14px"}),
    dict(name="a readout's label is on-dark and its value muted mono",
         on=B7_BENCH, sel=".ks3-rr-rovalue",
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "17px"}),
    dict(name="the bench panel is the nested dark panel, not the page ground",
         on=B7_BENCH, sel=".ks3-rr-panel",
         props={"background-color": "#3E3730"}),
    # ⚖️ A CHOSEN DIAL SETTING IS THE ALERT GROUND — Design's own `seg()`, and
    # a NARROWING of the platform's `.ks3-dark .ks3-option[aria-pressed]`,
    # which gives an alert border on the dark panel. Four dials with four thin
    # borders do not read as a state at a glance. If this row ever resolves to
    # #3E3730 the narrowing has been lost to source order and every bench in
    # the unit is showing its settings the platform's way.
    dict(name="a chosen dial setting is the alert ground with ink on it",
         on=B7_BENCH, sel='.ks3-rr-opt[aria-pressed="true"]',
         props={"background-color": "#FFC53D", "color": "#221E1B",
                "min-height": "44px"}),
    dict(name="an unchosen dial setting stays on the dark panel",
         on=B7_BENCH, sel='.ks3-rr-opt[aria-pressed="false"]',
         props={"background-color": "#3E3730", "color": "#FBF3E6",
                "min-height": "44px"}),
    # ⊕ THE CORRECTION, PINNED. `.ks3-reveal-btn` is ink on an ink border, and
    # this block's ground IS `--ks3-ink` — so the shipped rule paints an
    # invisible control. If this row ever resolves to #221E1B the test button
    # has disappeared into the block and the bench cannot be operated.
    dict(name="the test button is inverted on ink, not ink on ink",
         on=B7_BENCH, sel=".ks3-rr-test",
         props={"background-color": "#FBF3E6", "color": "#221E1B",
                "min-height": "44px"}),
    # ⚖️ THREE BARS, THREE COLOURS. The three readouts are three views of ONE
    # number and their widths are always identical, so colour is the only thing
    # telling them apart — the oxygen bar is the green one because it is the
    # readout you can actually watch. Measured on two of the three, because a
    # single rule painting all three would pass on one.
    dict(name="the oxygen bar is the ok green", on=B7_BENCH,
         sel='.ks3-rr-readout[data-tone="ok"] .ks3-rr-fill',
         props={"background-color": "#12A150"}),
    dict(name="the glucose bar is the alert, not the same green", on=B7_BENCH,
         sel='.ks3-rr-readout[data-tone="alert"] .ks3-rr-fill',
         props={"background-color": "#FFC53D"}),

    # ── b7-01 · the word summary, and the drawn arrow ──
    #
    # ⚠️ THE ARROW IS AN SVG STROKED `currentColor`, so this row is the whole
    # of Design's `color: var(--ks3-accent-text)` on the wrapper. If it ever
    # resolves to the ink the arrow has stopped being the accent; if the
    # element is absent the arrow has been typed, which the generator refuses
    # and the glyph audit would catch second.
    dict(name="the drawn reaction arrow is the accent text colour",
         on=B7_BENCH, sel=".ks3-eqn-arrowwrap",
         props={"color": "#A93411"}),
    dict(name="the summary's two sides are ink display type on the card",
         on=B7_BENCH, sel=".ks3-eqn-side",
         props={"color": "#221E1B", "font-family": "Bricolage Grotesque"}),
    dict(name="the reaction condition is a muted mono line under the row",
         on=B7_BENCH, sel=".ks3-eqn-condition",
         props={"color": "#5F564F", "font-family": "DM Mono",
                "font-size": "15px"}),
    dict(name="the equation sits on the card inside the band panel",
         on=B7_BENCH, sel=".ks3-eqn",
         props={"background-color": "#FFFCF5", "border-top-width": "2px",
                "border-top-color": "#221E1B"}),

    # ── b7-02 · leaf-tuner ──
    #
    # ⚖️ NO DRIVE ON THE VERDICT, and that is the instrument. The tuner has no
    # reveal: the opening leaf already earns a habitat and the panel is on
    # screen from the first paint. Measured at rest is measured in the state a
    # student meets.
    dict(name="the habitat verdict is the page ground on an ink block",
         on=B7_TUNER, sel=".ks3-lt-verdict:not([hidden])",
         props={"background-color": "#FBF3E6"}),
    dict(name="the verdict label is the accent eyebrow, not a marking colour",
         on=B7_TUNER, sel=".ks3-lt-verdict:not([hidden]) .ks3-lt-verdictlabel",
         props={"color": "#A93411", "font-family": "DM Mono",
                "font-size": "14px"}),
    dict(name="the habitat headline is ink display type on the cream panel",
         on=B7_TUNER, sel=".ks3-lt-verdict:not([hidden]) .ks3-lt-head",
         props={"color": "#221E1B", "font-family": "Bricolage Grotesque",
                "font-size": "23px"}),
    dict(name="the habitat reasoning reads in ink, not on-dark body",
         on=B7_TUNER, sel=".ks3-lt-verdict:not([hidden]) .ks3-lt-why",
         props={"color": "#221E1B", "font-size": "18px"}),
    # ⚖️ THE TWO BARS PULL AGAINST EACH OTHER AND ARE COLOURED FOR IT. Rate is
    # the ok green and water the alert; one colour on both would say the two
    # readouts are the same kind of number, which is the belief the whole
    # lesson exists to break.
    dict(name="the rate bar is the ok green", on=B7_TUNER,
         sel='.ks3-lt-readout[data-tone="ok"] .ks3-lt-fill',
         props={"background-color": "#12A150"}),
    dict(name="the water bar is the alert, not the same green", on=B7_TUNER,
         sel='.ks3-lt-readout[data-tone="alert"] .ks3-lt-fill',
         props={"background-color": "#FFC53D"}),
    dict(name="the tuner's readout labels are on-dark at 18px", on=B7_TUNER,
         sel=".ks3-lt-rolabel", props={"color": "#FBF3E6", "font-size": "18px"}),
    dict(name="the tuner's readout values are muted mono", on=B7_TUNER,
         sel=".ks3-lt-rovalue",
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "17px"}),
    # ⚖️ THE SAME NARROWING, MEASURED ON A SECOND PAGE. One rule serves all four
    # benches' dials, and measuring it on b7-01 alone would pass a b7-02 that
    # had been given a treatment of its own — which is the direction drift goes
    # when four instruments are written in one pass.
    dict(name="the tuner's chosen setting is the same alert ground",
         on=B7_TUNER, sel='.ks3-lt-opt[aria-pressed="true"]',
         props={"background-color": "#FFC53D", "color": "#221E1B",
                "min-height": "44px"}),
    # ⚖️ THE OAK BUTTON IS THE REVEAL, so the panel is measured once more AFTER
    # it — the only state on this instrument that a student reaches by pressing
    # something, and the one the whole lesson turns on.
    dict(name="the oak leaf's verdict is the same cream panel after the reveal",
         on=B7_TUNER, drive="b7-oak-pressed",
         sel=".ks3-lt-verdict:not([hidden])",
         props={"background-color": "#FBF3E6"}),
    dict(name="and its habitat reasoning is the same ink, not a copy",
         on=B7_TUNER, drive="b7-oak-pressed",
         sel=".ks3-lt-verdict:not([hidden]) .ks3-lt-why",
         props={"color": "#221E1B", "font-size": "18px"}),
    dict(name="the oak button is inverted on ink, not ink on ink",
         on=B7_TUNER, sel=".ks3-lt-oak",
         props={"background-color": "#FBF3E6", "color": "#221E1B",
                "min-height": "44px"}),

    # ── b7-03 · method-breaker ──
    dict(name="the method verdict is the page ground on an ink block",
         on=B7_METHOD, drive="b7-method-run", sel=".ks3-mb-verdict",
         props={"background-color": "#FBF3E6"}),
    dict(name="the result tag is the accent eyebrow, not a marking colour",
         on=B7_METHOD, drive="b7-method-run", sel=".ks3-mb-tag",
         props={"color": "#A93411", "font-family": "DM Mono",
                "font-size": "14px"}),
    dict(name="the result headline is ink display type on the cream panel",
         on=B7_METHOD, drive="b7-method-run", sel=".ks3-mb-head",
         props={"color": "#221E1B", "font-family": "Bricolage Grotesque",
                "font-size": "23px"}),
    dict(name="the result reasoning reads in ink, not on-dark body",
         on=B7_METHOD, drive="b7-method-run", sel=".ks3-mb-why",
         props={"color": "#221E1B", "font-size": "18px"}),
    # ⚖️ `conclude` IS THE FIELD THE LESSON TURNS ON — what the result licenses
    # you to say — and Design gives it its own rule above it. A fifth paragraph
    # inside the same cream panel is exactly the element B4 lost, so it is
    # pinned separately rather than left to the panel's rule.
    dict(name="the conclusion is ink under its own rule inside the panel",
         on=B7_METHOD, drive="b7-method-run", sel=".ks3-mb-conclude",
         props={"color": "#221E1B", "font-size": "18px",
                "border-top-width": "2px"}),
    # ⚠️⚠️ THE SAFETY BRANCH IS DRAWN AS A SAFETY BRANCH, AND THIS IS THE ROW
    # THAT SAYS SO. Its own words are "the test never happened"; if this ever
    # resolves to a transparent border the fire has been filed alongside a
    # spoiled pattern, which is precisely what NOTES-B7 flag 14 and MRB-233
    # exist to prevent. The drive reaches it by choosing the flame.
    dict(name="the safety branch takes the accent outline a data fault does not",
         on=B7_METHOD, drive="b7-method-flamed",
         sel='.ks3-mb-verdict[data-kind="safety"]',
         props={"border-top-color": "#E4572E", "border-top-width": "2px"}),
    dict(name="a step's title is on-dark and its detail muted", on=B7_METHOD,
         sel=".ks3-mb-stepdetail",
         props={"color": "#C6B9A7", "font-size": "17px"}),
    dict(name="a step's number chip is a muted outline, not a filled mark",
         on=B7_METHOD, sel=".ks3-mb-num",
         props={"color": "#C6B9A7", "border-top-color": "#C6B9A7",
                "font-family": "Bricolage Grotesque"}),
    dict(name="the run button is inverted on ink, not ink on ink",
         on=B7_METHOD, sel=".ks3-mb-run",
         props={"background-color": "#FBF3E6", "color": "#221E1B",
                "min-height": "44px"}),

    # ── b7-04 · trace-it-back ──
    dict(name="the chain verdict is the page ground on an ink block",
         on=B7_TRACE, drive="b7-chain-traced", sel=".ks3-tb-verdict",
         props={"background-color": "#FBF3E6", "color": "#221E1B",
                "font-size": "18px"}),
    dict(name="the steps-back line is the alert mono line", on=B7_TRACE,
         sel=".ks3-tb-food:not([hidden]) .ks3-tb-steps",
         props={"color": "#FFC53D", "font-family": "DM Mono",
                "font-size": "16px"}),
    dict(name="the food's name is on-dark at 21px", on=B7_TRACE,
         sel=".ks3-tb-food:not([hidden]) .ks3-tb-name",
         props={"color": "#FBF3E6", "font-size": "21px"}),
    # ⚖️ AN UNREACHED LINK DIMS AND STAYS ON-DARK. It is not a wrong answer and
    # it is not absent: the whole chain is drawn from the start so a student
    # reads how far there is to go. If the opacity ever resolves to 1 the
    # instrument has given away where the chain ends before the first press.
    # ⊕ MRB-257 · audit 3.7 — THIS ROW PINNED THE DEFECT AT 0.45.
    # The reasoning above is right and the number was wrong: a row a
    # student is meant to READ, in order to see how far there is to go,
    # composited `--ks3-on-dark-muted` to #7B7266 on the dark panel =
    # 2.48:1, and the text is the science itself. `--ks3-dim-ahead` is
    # .8, which lands 4.51:1. The row is not deleted and not loosened —
    # it still asserts that the dim EXISTS, which is what stops the bench
    # giving away where the chain ends before the first press; it now
    # asserts the value that is also legible.
    dict(name="an unreached link dims and keeps its on-dark name", on=B7_TRACE,
         sel=".ks3-tb-food:not([hidden]) .ks3-tb-link:not([data-shown])",
         props={"opacity": "0.8"}),
    dict(name="an unreached link's name is muted, not headline", on=B7_TRACE,
         sel=(".ks3-tb-food:not([hidden]) "
              ".ks3-tb-link:not([data-shown]) .ks3-tb-linkname"),
         props={"color": "#C6B9A7", "font-size": "19px"}),
    # ⚖️ A REVEALED LINK LIGHTS ITS CHIP AND ITS NAME, and the note under it is
    # on-dark BODY rather than the headline colour — over four lines that is
    # the glare `--ks3-on-dark-body` exists to avoid.
    dict(name="a revealed link's chip is the alert with ink on it", on=B7_TRACE,
         sel=".ks3-tb-food:not([hidden]) .ks3-tb-link[data-shown] .ks3-tb-num",
         props={"background-color": "#FFC53D", "color": "#221E1B"}),
    dict(name="a revealed link's note reads in on-dark body", on=B7_TRACE,
         sel=".ks3-tb-food:not([hidden]) .ks3-tb-link[data-shown] .ks3-tb-note",
         props={"color": "#E7DECE", "font-size": "18px"}),
    dict(name="the plate label is muted mono on ink", on=B7_TRACE,
         sel=".ks3-tb-tabslabel",
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "14px"}),
    dict(name="the chosen food tab is the same alert ground", on=B7_TRACE,
         sel='.ks3-tb-tab[aria-pressed="true"]',
         props={"background-color": "#FFC53D", "color": "#221E1B",
                "min-height": "44px"}),
    dict(name="the step button is inverted on ink, not ink on ink",
         on=B7_TRACE, sel=".ks3-tb-back",
         props={"background-color": "#FBF3E6", "color": "#221E1B",
                "min-height": "44px"}),
    # ═══ END B7 ═══ rows
    # ══ B8 · Respiration (⊕ MRB-248) ════════════════════════════════════
    #
    # ⚠️ THESE ROWS EXIST BECAUSE OF THE SPECIFICITY TRAP, AND THEY ARE AIMED
    # AT IT. All five B8 instruments sit on `ks3-dark`. `.ks3-dark p` is
    # (0,1,1) and beats a bare instrument class at (0,1,0) — so a rule written
    # as `.ks3-ml-total { color: … }` LOSES to the dark-ground default and
    # ships a label at roughly 1.2:1 that no grep will ever find, because the
    # CSS is right there in the file saying the correct thing. Only a computed
    # read catches it. Every rule below is therefore asserted against the
    # element as the BROWSER resolves it, not as the stylesheet declares it.
    #
    # This is the trap that produced 200 defects across 46 pages, and was then
    # re-laid hours later inside a section whose own comment claimed every rule
    # was scoped. The comment is not evidence. The measurement is.
    dict(name="B8 mass-ledger · column head on ink", on=B8_LEDGER,
         sel=".ks3-ml-colhead", props={"font-family": "DM Mono"}),
    dict(name="B8 mass-ledger · row name resolves on ink, not to .ks3-dark p",
         on=B8_LEDGER, sel=".ks3-ml-rowname", props={"color": "#FBF3E6"}),
    dict(name="B8 cell-demand · spend bar name on ink", on=B8_DEMAND,
         sel=".ks3-cd-spendname", props={"color": "#FBF3E6"}),
    dict(name="B8 oxygen-debt · bar name resolves on ink", on=B8_DEBT,
         sel=".ks3-od-barname", props={"color": "#FBF3E6"}),
    dict(name="B8 oxygen-debt · bar value is mono on ink", on=B8_DEBT,
         sel=".ks3-od-barvalue", props={"font-family": "DM Mono"}),
    # ⚖️ NO BRANCH IS STYLED AS AN ERROR — the yeast open-and-stirred branch is
    # how yeast is MANUFACTURED. This row pins the reaction line to the ordinary
    # on-ink treatment so a later pass cannot quietly introduce a failure tone.
    dict(name="B8 fermenter · reaction line takes no error tone", on=B8_FERM,
         sel=".ks3-fm-line", props={"font-size": "20px", "font-weight": "700"}),
    dict(name="B8 fermenter · rate readout is mono on ink", on=B8_FERM,
         sel=".ks3-fm-rate", props={"font-family": "DM Mono"}),
    # ⚖️ THE ROUTE BENCH HAS NO CORRECT-ANSWER STYLING AND MUST NOT ACQUIRE
    # ANY. A route button is an ordinary `.ks3-option` whether the student had
    # it or not; the verdict panel names the answer in words. MRB-196 R10 and
    # the house rule — only the ladder marks correctness. If a later pass paints
    # this green, this row is what stops it.
    dict(name="B8 route-decider · case text resolves on ink", on=B8_ROUTE,
         sel=".ks3-rd-text", props={"color": "#FBF3E6", "font-size": "18px"}),
    dict(name="B8 route-decider · verdict word is mono on ink", on=B8_ROUTE,
         sel=".ks3-rd-word", props={"font-family": "DM Mono",
                                    "color": "#FBF3E6"}),
    dict(name="B8 route-decider · the why line is body on ink", on=B8_ROUTE,
         sel=".ks3-rd-why", props={"font-size": "17px"}),
    dict(name="B8 route-decider · the case label row is mono muted",
         on=B8_ROUTE, sel=".ks3-rd-caseslabel",
         props={"font-family": "DM Mono", "font-size": "14px"}),

    # ══ B9 · Ecosystems and interdependence (⊕ MRB-250) ═════════════════
    #
    # ⚠️ THESE ROWS EXIST BECAUSE B8 SHIPPED WITHOUT THEM. B7's two flagship
    # instruments carry 23 and 24 assertions apiece; B8's five carry 1, 2, 2, 3
    # and 4 — twelve across five instruments, which is not coverage, it is a
    # sample. The kinds gate stayed green throughout, because a dispatch entry
    # is not a component and a green gate over an unmeasured component says
    # nothing at all. Every B9 instrument below carries a full state sweep:
    # resting, chosen, revealed, spent, and every state the science depends on.
    #
    # ⚠️ AND THEY ARE AIMED AT THE SPECIFICITY TRAP. All six B9 instruments sit
    # on `ks3-dark`. `.ks3-dark p` is (0,1,1) and beats a bare instrument class
    # at (0,1,0) — so a rule written as `.ks3-cl-energy { color: … }` LOSES to
    # the dark-ground default and ships a figure at roughly 1.2:1 that no grep
    # will ever find, because the CSS is right there saying the correct thing.
    # Only a computed read catches it. Every rule below is asserted against the
    # element as the BROWSER resolves it, not as the stylesheet declares it.

    # ── b9-01 · chain-ledger ──
    dict(name="B9 chain-ledger · the chain label is muted mono on ink",
         on=B9_CHAIN, sel=".ks3-cl-tabslabel",
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "14px"}),
    # ⚖️ A CHOSEN TAB IS THE ALERT GROUND, which is Design's `seg()` and NOT
    # the platform's alert border. Still not a mark: it says "this is the
    # chain you are looking at", never "this is correct".
    dict(name="B9 chain-ledger · the chosen chain tab is the alert ground",
         on=B9_CHAIN, sel='.ks3-cl-tab[aria-pressed="true"]',
         props={"background-color": "#FFC53D", "color": "#221E1B",
                "min-height": "44px"}),
    dict(name="B9 chain-ledger · an unchosen tab stays on the panel ground",
         on=B9_CHAIN, sel='.ks3-cl-tab[aria-pressed="false"]',
         props={"background-color": "#3E3730", "color": "#FBF3E6"}),
    # ⚖️⚖️ THE PRODUCER IS DRAWN AT THE BOTTOM AND THIS IS THE ROW THAT SAYS
    # SO. `column-reverse` is the claim the lesson makes about which way energy
    # travels, not a layout preference: `#s-think`'s first quote is that arrows
    # point at what the animal eats, and it is the single most-marked error in
    # the topic. If this ever resolves to `column` the bench is drawing the
    # same figures making the opposite argument, and nothing else would notice.
    dict(name="B9 chain-ledger · the producer is drawn at the BOTTOM",
         on=B9_CHAIN, sel=".ks3-cl-levels:not([hidden])",
         props={"display": "flex", "flex-direction": "column-reverse"}),
    # ⚖️ AN UNREACHED LEVEL DIMS AND STAYS ON-DARK. It is not a wrong answer
    # and it is not absent: the whole chain is drawn from the start so a
    # student reads how far there is to go. If the opacity resolves to 1 the
    # bench has given away where the chain ends before the first press.
    # ⊕ MRB-257 · audit 3.5 — THIS ROW PINNED THE DEFECT AT 0.45.
    # The reasoning above is right and the number was wrong: a row a
    # student is meant to READ, in order to see how far there is to go,
    # composited `--ks3-on-dark-muted` to #7B7266 on the dark panel =
    # 2.48:1, and the text is the science itself. `--ks3-dim-ahead` is
    # .8, which lands 4.51:1. The row is not deleted and not loosened —
    # it still asserts that the dim EXISTS, which is what stops the bench
    # giving away where the chain ends before the first press; it now
    # asserts the value that is also legible.
    dict(name="B9 chain-ledger · an unreached level dims and takes no outline",
         on=B9_CHAIN,
         sel=".ks3-cl-levels:not([hidden]) .ks3-cl-level:not([data-shown])",
         props={"opacity": "0.8", "border-top-color": "rgba(0, 0, 0, 0)"}),
    dict(name="B9 chain-ledger · an unreached level's name is muted",
         on=B9_CHAIN,
         sel=(".ks3-cl-levels:not([hidden]) "
              ".ks3-cl-level:not([data-shown]) .ks3-cl-levelname"),
         props={"color": "#C6B9A7", "font-size": "19px"}),
    dict(name="B9 chain-ledger · a revealed level's name is on-dark headline",
         on=B9_CHAIN,
         sel=(".ks3-cl-levels:not([hidden]) "
              ".ks3-cl-level[data-shown] .ks3-cl-levelname"),
         props={"color": "#FBF3E6", "font-size": "19px",
                "font-weight": "700"}),
    dict(name="B9 chain-ledger · the level just reached takes the alert outline",
         on=B9_CHAIN,
         sel=".ks3-cl-levels:not([hidden]) .ks3-cl-level[data-top]",
         props={"border-top-color": "#FFC53D", "border-top-width": "2px"}),
    dict(name="B9 chain-ledger · the trophic role is muted mono, not body",
         on=B9_CHAIN,
         sel=".ks3-cl-levels:not([hidden]) .ks3-cl-levelrole",
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "16px"}),
    # ⚖️ THE ENERGY FIGURE TAKES THE ALERT AND THE PERCENTAGE BESIDE IT DOES
    # NOT. The number falling by a factor of ten is the one the eye should land
    # on; the percentage restates it. Two mono lines in one colour would make
    # them read as one quantity printed twice.
    dict(name="B9 chain-ledger · the energy figure is the alert mono line",
         on=B9_CHAIN, sel=".ks3-cl-levels:not([hidden]) [data-cl-energy]",
         props={"color": "#FFC53D", "font-family": "DM Mono",
                "font-size": "17px"}),
    dict(name="B9 chain-ledger · the percentage beside it is muted, not alert",
         on=B9_CHAIN, sel=".ks3-cl-levels:not([hidden]) [data-cl-pct]",
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "15px"}),
    dict(name="B9 chain-ledger · the energy bar is the alert fill",
         on=B9_CHAIN, sel=".ks3-cl-levels:not([hidden]) .ks3-cl-bar",
         props={"background-color": "#FFC53D"}),
    dict(name="B9 chain-ledger · the bar sits in a translucent well",
         on=B9_CHAIN, sel=".ks3-cl-levels:not([hidden]) .ks3-cl-track",
         props={"height": "16px",
                "background-color": "rgba(255, 255, 255, 0.08)"}),
    dict(name="B9 chain-ledger · the level note reads in on-dark body",
         on=B9_CHAIN, sel=".ks3-cl-levels:not([hidden]) .ks3-cl-note",
         props={"color": "#E7DECE", "font-size": "17px"}),
    dict(name="B9 chain-ledger · the ledger sits on the nested dark panel",
         on=B9_CHAIN, sel=".ks3-cl-panel",
         props={"background-color": "#3E3730"}),
    dict(name="B9 chain-ledger · the step button is inverted on ink",
         on=B9_CHAIN, sel=".ks3-cl-up",
         props={"background-color": "#FBF3E6", "color": "#221E1B",
                "min-height": "44px"}),
    dict(name="B9 chain-ledger · the reset button is inverted on ink",
         on=B9_CHAIN, sel=".ks3-cl-reset",
         props={"background-color": "#FBF3E6", "color": "#221E1B",
                "min-height": "44px"}),
    # ⚖️ THE VERDICT IS THE PAGE GROUND ON AN INK BLOCK — cream inside ink,
    # which is the one place in this unit where the text colour has to be INK
    # and not on-dark. It is the element the whole climb exists to reach.
    dict(name="B9 chain-ledger · the verdict is the page ground on an ink block",
         on=B9_CHAIN, drive="b9-chain-topped",
         sel=".ks3-cl-verdict:not([hidden])",
         props={"background-color": "#FBF3E6", "color": "#221E1B",
                "font-size": "18px"}),
    dict(name="B9 chain-ledger · the spent step button dims", on=B9_CHAIN,
         drive="b9-chain-topped", sel=".ks3-cl-up[disabled]",
         props={"opacity": "0.45"}),
    # ⊕ MRB-257 · audit 3.13 — the lit ground was rgba(255,255,255,.10), which
    # composites to #514B45 and put four revealed readouts at 4.46:1 against a
    # 4.5 bar. .06 composites to #4A433C = 5.05:1. The row still asserts that
    # the top level IS lit — which is the claim — at the value that lets the
    # figures on it be read. Four instruments carry the same wash; this is the
    # one with a row.
    dict(name="B9 chain-ledger · the top level lights its ground", on=B9_CHAIN,
         drive="b9-chain-topped",
         sel=".ks3-cl-levels:not([hidden]) .ks3-cl-level[data-top]",
         props={"background-color": "rgba(255, 255, 255, 0.06)"}),

    # ── b9-02 · cycle-runner ──
    # ⚖️⚖️ THE TWO SERIES ARE TWO COLOURS AND THE CAPTION NAMES THEM BY
    # COLOUR — "amber = rabbits · green = foxes". These four rows are what
    # stops the caption becoming a lie. If either readout or either bar ever
    # resolves to the other's hue, or to the same hue, the chart stops being
    # readable at all and the LAG — which is the entire lesson and what both
    # marked rungs test — becomes invisible.
    dict(name="B9 cycle-runner · the prey readout is the amber the caption names",
         on=B9_CYCLE, sel='.ks3-cy-live[data-series="prey"]',
         props={"color": "#FFC53D", "font-size": "20px",
                "font-weight": "700"}),
    # ⊕ MRB-252 (RULED) · audit 3.4 — THIS ROW PINNED #12A150 AS TEXT, which
    # is the value the token file forbids as text and the value the audit
    # measured at 3.48:1 on this ground. A gate holding a defect in place is
    # not weakened by correcting it: re-pointed at `--ks3-ok-dark`, and the
    # `font-size` and `font-weight` stay because they are what make it text
    # rather than a mark, and therefore what makes 4.5:1 the bar.
    dict(name="B9 cycle-runner · the predator readout is the green it names",
         on=B9_CYCLE, sel='.ks3-cy-live[data-series="pred"]',
         props={"color": "#40DD84", "font-size": "20px",
                "font-weight": "700"}),
    dict(name="B9 cycle-runner · the prey bar is amber and flat-bottomed",
         on=B9_CYCLE, sel='.ks3-cy-bar[data-series="prey"]',
         props={"background-color": "#FFC53D",
                "border-top-left-radius": "2px",
                "border-bottom-left-radius": "0px"}),
    dict(name="B9 cycle-runner · the predator bar is green", on=B9_CYCLE,
         sel='.ks3-cy-bar[data-series="pred"]',
         props={"background-color": "#12A150"}),
    # ⚖️ THE CHART IS A FIXED BAND AND THE BARS GROW FROM ITS FLOOR. A chart
    # that changed height with the data would make two years incomparable,
    # which is the one comparison the block is for.
    dict(name="B9 cycle-runner · the chart is a fixed band, bars from the floor",
         on=B9_CYCLE, sel=".ks3-cy-chart",
         props={"display": "flex", "height": "150px",
                "align-items": "flex-end"}),
    dict(name="B9 cycle-runner · a year is a PAIR of bars, not one",
         on=B9_CYCLE, sel=".ks3-cy-year",
         props={"display": "flex", "align-items": "flex-end",
                "min-width": "0px"}),
    dict(name="B9 cycle-runner · the caption is muted mono in caps",
         on=B9_CYCLE, sel=".ks3-cy-caption",
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "14px", "text-transform": "uppercase"}),
    dict(name="B9 cycle-runner · the note reads in on-dark body", on=B9_CYCLE,
         sel=".ks3-cy-note",
         props={"color": "#E7DECE", "font-size": "18px",
                "line-height": "27.9px"}),
    dict(name="B9 cycle-runner · the field sits on the nested dark panel",
         on=B9_CYCLE, sel=".ks3-cy-panel",
         props={"background-color": "#3E3730"}),
    dict(name="B9 cycle-runner · the year buttons are inverted on ink",
         on=B9_CYCLE, sel=".ks3-cy-btn",
         props={"background-color": "#FBF3E6", "color": "#221E1B",
                "min-height": "44px"}),
    # ⚖️ AND AFTER THE CULL, THIRTY YEARS ON, ALL OF IT STILL HOLDS. This is
    # the state the carrying-capacity argument is read in — rabbits at the
    # ceiling, foxes at zero — and it is the state a "tidy the chart" revision
    # would break first, because it is the only one where one series is flat.
    dict(name="B9 cycle-runner · the amber survives thirty years without foxes",
         on=B9_CYCLE, drive="b9-cycle-culled",
         sel='.ks3-cy-bar[data-series="prey"]',
         props={"background-color": "#FFC53D"}),
    dict(name="B9 cycle-runner · the green series is still drawn at extinction",
         on=B9_CYCLE, drive="b9-cycle-culled",
         sel='.ks3-cy-bar[data-series="pred"]',
         props={"background-color": "#12A150"}),
    dict(name="B9 cycle-runner · the chart band does not grow with the data",
         on=B9_CYCLE, drive="b9-cycle-culled", sel=".ks3-cy-chart",
         props={"height": "150px"}),
    dict(name="B9 cycle-runner · the ceiling note reads in on-dark body",
         on=B9_CYCLE, drive="b9-cycle-culled", sel=".ks3-cy-note",
         props={"color": "#E7DECE"}),
    dict(name="B9 cycle-runner · the fox readout keeps its green at zero",
         on=B9_CYCLE, drive="b9-cycle-culled",
         sel='.ks3-cy-live[data-series="pred"]', props={"color": "#40DD84"}),

    # ── b9-03 · remove-a-species ──
    dict(name="B9 remove-a-species · the web label is muted mono on ink",
         on=B9_REMOVE, sel=".ks3-rs-weblabel",
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "14px"}),
    # ⚖️ THE WEB IS PROSE IN A GRID, NOT A DRAWN GRAPH. Eight who-eats-whom
    # lines, no adjacency structure — which is what lets the bees' line sit in
    # the list as an equal rather than as a missing edge. See NOTES flag 17:
    # the drawn web is Mide's to rule on and is not invented here.
    dict(name="B9 remove-a-species · the web is a prose grid", on=B9_REMOVE,
         sel=".ks3-rs-weblines", props={"display": "grid"}),
    dict(name="B9 remove-a-species · a web line reads in on-dark body",
         on=B9_REMOVE, sel=".ks3-rs-webline",
         props={"color": "#E7DECE", "font-size": "17px"}),
    dict(name="B9 remove-a-species · the remove label is muted mono",
         on=B9_REMOVE, sel=".ks3-rs-tabslabel",
         props={"color": "#C6B9A7", "font-family": "DM Mono"}),
    dict(name="B9 remove-a-species · the chosen species tab is the alert ground",
         on=B9_REMOVE, sel='.ks3-rs-tab[aria-pressed="true"]',
         props={"background-color": "#FFC53D", "color": "#221E1B",
                "min-height": "44px"}),
    dict(name="B9 remove-a-species · the consequences sit on the dark panel",
         on=B9_REMOVE, sel=".ks3-rs-body",
         props={"background-color": "#3E3730"}),
    dict(name="B9 remove-a-species · the headline is on-dark at 21px",
         on=B9_REMOVE, sel="[data-rs-panel]:not([hidden]) [data-rs-headline]",
         props={"color": "#FBF3E6", "font-size": "21px",
                "font-weight": "700"}),
    dict(name="B9 remove-a-species · the why line is muted, not headline",
         on=B9_REMOVE, sel="[data-rs-panel]:not([hidden]) .ks3-rs-why",
         props={"color": "#C6B9A7", "font-size": "18px"}),
    dict(name="B9 remove-a-species · an unreached round dims and has no outline",
         on=B9_REMOVE,
         sel="[data-rs-panel]:not([hidden]) .ks3-rs-round:not([data-shown])",
         props={"opacity": "0.8", "border-top-color": "rgba(0, 0, 0, 0)"}),
    dict(name="B9 remove-a-species · an unreached round chip is a muted outline",
         on=B9_REMOVE,
         sel=("[data-rs-panel]:not([hidden]) "
              ".ks3-rs-round:not([data-shown]) .ks3-rs-num"),
         props={"color": "#C6B9A7", "background-color": "rgba(0, 0, 0, 0)",
                "border-top-color": "#C6B9A7"}),
    dict(name="B9 remove-a-species · an unreached round title is muted",
         on=B9_REMOVE,
         sel=("[data-rs-panel]:not([hidden]) "
              ".ks3-rs-round:not([data-shown]) .ks3-rs-roundtitle"),
         props={"color": "#C6B9A7", "font-size": "19px"}),
    dict(name="B9 remove-a-species · the step button is inverted on ink",
         on=B9_REMOVE, sel=".ks3-rs-next",
         props={"background-color": "#FBF3E6", "color": "#221E1B",
                "min-height": "44px"}),
    dict(name="B9 remove-a-species · the put-it-back button is inverted on ink",
         on=B9_REMOVE, sel=".ks3-rs-reset",
         props={"background-color": "#FBF3E6", "color": "#221E1B"}),
    dict(name="B9 remove-a-species · a followed round fills its chip in alert",
         on=B9_REMOVE, drive="b9-web-followed",
         sel=("[data-rs-panel]:not([hidden]) "
              ".ks3-rs-round[data-shown] .ks3-rs-num"),
         props={"background-color": "#FFC53D", "color": "#221E1B",
                "border-top-color": "#FFC53D"}),
    dict(name="B9 remove-a-species · a followed round title lifts to on-dark",
         on=B9_REMOVE, drive="b9-web-followed",
         sel=("[data-rs-panel]:not([hidden]) "
              ".ks3-rs-round[data-shown] .ks3-rs-roundtitle"),
         props={"color": "#FBF3E6"}),
    dict(name="B9 remove-a-species · the consequence text is on-dark body",
         on=B9_REMOVE, drive="b9-web-followed",
         sel=("[data-rs-panel]:not([hidden]) "
              ".ks3-rs-round[data-shown] .ks3-rs-roundbody"),
         props={"color": "#E7DECE", "font-size": "18px"}),
    # ⊕ MRB-257 · audit 3.13 — the same wash, two instruments further on. .10
    # composited to #514B45 and put the readouts on it at 4.46:1; .06 is
    # #4A433C at 5.05:1. The claim ("the round just reached is lit") stands.
    dict(name="B9 remove-a-species · the round just reached is outlined in alert",
         on=B9_REMOVE, drive="b9-web-followed",
         sel="[data-rs-panel]:not([hidden]) .ks3-rs-round[data-cur]",
         props={"border-top-color": "#FFC53D",
                "background-color": "rgba(255, 255, 255, 0.06)"}),
    dict(name="B9 remove-a-species · the verdict is the page ground on ink",
         on=B9_REMOVE, drive="b9-web-followed",
         sel="[data-rs-panel]:not([hidden]) [data-rs-verdict]:not([hidden])",
         props={"background-color": "#FBF3E6", "color": "#221E1B",
                "font-size": "18px"}),
    dict(name="B9 remove-a-species · the spent step button dims", on=B9_REMOVE,
         drive="b9-web-followed", sel=".ks3-rs-next[disabled]",
         props={"opacity": "0.45"}),

    # ── b9-04 · supermarket-shelf ──
    dict(name="B9 supermarket-shelf · the shelf sits on the nested dark panel",
         on=B9_SHELF, sel=".ks3-ss", props={"background-color": "#3E3730"}),
    dict(name="B9 supermarket-shelf · the twelve foods are a wrapping grid",
         on=B9_SHELF, sel=".ks3-ss-shelf", props={"display": "grid"}),
    dict(name="B9 supermarket-shelf · a surviving food is outlined and upright",
         on=B9_SHELF, sel=".ks3-ss-food:not([data-gone])",
         props={"border-top-color": "#C6B9A7", "opacity": "1",
                "text-decoration-line": "none"}),
    dict(name="B9 supermarket-shelf · a surviving food's name is on-dark",
         on=B9_SHELF, sel=".ks3-ss-food:not([data-gone]) .ks3-ss-foodname",
         props={"color": "#FBF3E6", "font-size": "18px",
                "font-weight": "700"}),
    # ⚖️ AT FULL POLLINATION THE TILE READS *HOW*, and it reads it in the same
    # mono the status will use — so the dial doubles as the teaching label and
    # the swap from "wind-pollinated" to "gone" is a change of words rather
    # than a change of component.
    dict(name="B9 supermarket-shelf · the how/status line is mono caps on ink",
         on=B9_SHELF, sel=".ks3-ss-food:not([data-gone]) .ks3-ss-foodstatus",
         props={"color": "#FBF3E6", "font-family": "DM Mono",
                "font-size": "14px", "text-transform": "uppercase"}),
    # ⚖️⚖️ TWO BARS, SIDE BY SIDE, NEVER COMBINED. The gap between them IS the
    # lesson. `b9-shelf-emptied` squeezes the container and proves they WRAP to
    # two rows rather than merging or dropping one, which is the failure a
    # default-width measurement cannot see.
    dict(name="B9 supermarket-shelf · the two bars are a grid, never one bar",
         on=B9_SHELF, sel=".ks3-ss-bars", props={"display": "grid"}),
    dict(name="B9 supermarket-shelf · the calorie label is on-dark at 17px",
         on=B9_SHELF, sel='[data-ss-bar="cal"] .ks3-ss-barlabel',
         props={"color": "#FBF3E6", "font-size": "17px",
                "font-weight": "600"}),
    dict(name="B9 supermarket-shelf · the percentage is muted mono",
         on=B9_SHELF, sel='[data-ss-bar="cal"] [data-ss-value]',
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "17px"}),
    dict(name="B9 supermarket-shelf · the calorie fill is the green",
         on=B9_SHELF, sel='[data-ss-bar="cal"] .ks3-ss-fill',
         props={"background-color": "#12A150"}),
    dict(name="B9 supermarket-shelf · the vitamin fill is the amber",
         on=B9_SHELF, sel='[data-ss-bar="vit"] .ks3-ss-fill',
         props={"background-color": "#FFC53D"}),
    dict(name="B9 supermarket-shelf · the bar wells are 18px", on=B9_SHELF,
         sel='[data-ss-bar="cal"] .ks3-ss-track', props={"height": "18px"}),
    dict(name="B9 supermarket-shelf · the note reads in on-dark body",
         on=B9_SHELF, sel=".ks3-ss-note",
         props={"color": "#E7DECE", "font-size": "18px"}),
    dict(name="B9 supermarket-shelf · the remove button is inverted on ink",
         on=B9_SHELF, sel=".ks3-ss-toggle",
         props={"background-color": "#FBF3E6", "color": "#221E1B",
                "min-height": "44px"}),
    # ⚖️ A FAILED CROP IS STRUCK THROUGH AS WELL AS AMBER, so colour is never
    # the only signal (R2). And it is still not a mark: nothing the student
    # does here is right or wrong, and what the amber says is that this crop
    # has failed.
    dict(name="B9 supermarket-shelf · a failed crop is amber AND struck through",
         on=B9_SHELF, drive="b9-shelf-emptied", sel=".ks3-ss-food[data-gone]",
         props={"border-top-color": "#FFC53D", "opacity": "0.6",
                "text-decoration-line": "line-through"}),
    dict(name="B9 supermarket-shelf · a failed crop's name drops to muted",
         on=B9_SHELF, drive="b9-shelf-emptied",
         sel=".ks3-ss-food[data-gone] .ks3-ss-foodname",
         props={"color": "#C6B9A7"}),
    dict(name="B9 supermarket-shelf · a failed crop's status drops to muted",
         on=B9_SHELF, drive="b9-shelf-emptied",
         sel=".ks3-ss-food[data-gone] .ks3-ss-foodstatus",
         props={"color": "#C6B9A7"}),
    dict(name="B9 supermarket-shelf · the calorie bar keeps its own green",
         on=B9_SHELF, drive="b9-shelf-emptied",
         sel='[data-ss-bar="cal"] .ks3-ss-fill',
         props={"background-color": "#12A150"}),
    dict(name="B9 supermarket-shelf · the vitamin bar keeps its own amber",
         on=B9_SHELF, drive="b9-shelf-emptied",
         sel='[data-ss-bar="vit"] .ks3-ss-fill',
         props={"background-color": "#FFC53D"}),
    dict(name="B9 supermarket-shelf · the gap note reads in on-dark body",
         on=B9_SHELF, drive="b9-shelf-emptied", sel=".ks3-ss-note",
         props={"color": "#E7DECE"}),

    # ── b9-05 · bioaccumulation ──
    dict(name="B9 bioaccumulation · the chemical label is muted mono on ink",
         on=B9_TOXIC, sel=".ks3-ba-tabslabel",
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "14px"}),
    dict(name="B9 bioaccumulation · the chosen setting is the alert ground",
         on=B9_TOXIC, sel='.ks3-ba-tab[aria-pressed="true"]',
         props={"background-color": "#FFC53D", "color": "#221E1B",
                "min-height": "44px"}),
    # ⚖️ THE SAME LADDER AS b9-01, THE SAME WAY UP. Water at the bottom,
    # ospreys at the top, because this bench is b9-01's arithmetic run in the
    # other direction and the two are deliberately the same shape.
    dict(name="B9 bioaccumulation · the lake water is drawn at the BOTTOM",
         on=B9_TOXIC, sel=".ks3-ba-levels",
         props={"flex-direction": "column-reverse"}),
    dict(name="B9 bioaccumulation · the setting's note is muted, not body",
         on=B9_TOXIC, sel=".ks3-ba-chemnote",
         props={"color": "#C6B9A7", "font-size": "18px"}),
    dict(name="B9 bioaccumulation · an unreached level dims and has no outline",
         on=B9_TOXIC, sel=".ks3-ba-level:not([data-shown])",
         props={"opacity": "0.8", "border-top-color": "rgba(0, 0, 0, 0)"}),
    dict(name="B9 bioaccumulation · an unreached level's name is muted",
         on=B9_TOXIC, sel=".ks3-ba-level:not([data-shown]) .ks3-ba-name",
         props={"color": "#C6B9A7", "font-size": "19px"}),
    dict(name="B9 bioaccumulation · a revealed level's name is on-dark",
         on=B9_TOXIC, sel=".ks3-ba-level[data-shown] .ks3-ba-name",
         props={"color": "#FBF3E6"}),
    dict(name="B9 bioaccumulation · the level just reached is outlined in alert",
         on=B9_TOXIC, sel=".ks3-ba-level[data-cur]",
         props={"border-top-color": "#FFC53D", "border-top-width": "2px"}),
    # ⚖️ THE `eats` LINE IS THE MECHANISM AND IT IS ON SCREEN BEFORE THE
    # NUMBERS. "Eat hundreds of perch a year" is WHY the concentration
    # multiplies rather than merely persisting, and it stays legible on an
    # unreached row so the student can read the chain before climbing it.
    dict(name="B9 bioaccumulation · the eats line is muted mono, always on",
         on=B9_TOXIC, sel=".ks3-ba-eats",
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "16px"}),
    dict(name="B9 bioaccumulation · the concentration is the alert mono line",
         on=B9_TOXIC, sel="[data-ba-ppm]",
         props={"color": "#FFC53D", "font-family": "DM Mono",
                "font-size": "18px"}),
    # ⚖️⚖️ A SAFE ROW IS MUTED — INCLUDING EVERY ROW OF THE ×1 CONTROL. If this
    # ever resolves to the alert the control stops being flat, the comparison
    # the lesson rests on disappears, and the bench starts saying the chemical
    # is dangerous everywhere. That is the belief `#s-think` exists to break.
    dict(name="B9 bioaccumulation · a safe level's verdict is muted, not alert",
         on=B9_TOXIC,
         sel=".ks3-ba-level:not([data-harmful]) [data-ba-lvlverdict]",
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "15px"}),
    dict(name="B9 bioaccumulation · a safe level's bar is muted, not alert",
         on=B9_TOXIC, sel=".ks3-ba-level:not([data-harmful]) .ks3-ba-bar",
         props={"background-color": "#C6B9A7"}),
    dict(name="B9 bioaccumulation · the chain sits on the nested dark panel",
         on=B9_TOXIC, sel=".ks3-ba-panel",
         props={"background-color": "#3E3730"}),
    dict(name="B9 bioaccumulation · the step button is inverted on ink",
         on=B9_TOXIC, sel=".ks3-ba-up",
         props={"background-color": "#FBF3E6", "color": "#221E1B",
                "min-height": "44px"}),
    dict(name="B9 bioaccumulation · a harmful level's verdict takes the alert",
         on=B9_TOXIC, drive="b9-chain-poisoned",
         sel=".ks3-ba-level[data-harmful] [data-ba-lvlverdict]",
         props={"color": "#FFC53D"}),
    dict(name="B9 bioaccumulation · a harmful level's bar takes the alert",
         on=B9_TOXIC, drive="b9-chain-poisoned",
         sel=".ks3-ba-level[data-harmful] .ks3-ba-bar",
         props={"background-color": "#FFC53D"}),
    dict(name="B9 bioaccumulation · the verdict is the page ground on ink",
         on=B9_TOXIC, drive="b9-chain-poisoned",
         sel=".ks3-ba-verdict:not([hidden])",
         props={"background-color": "#FBF3E6", "color": "#221E1B",
                "font-size": "18px"}),
    dict(name="B9 bioaccumulation · the spent step button dims", on=B9_TOXIC,
         drive="b9-chain-poisoned", sel=".ks3-ba-up[disabled]",
         props={"opacity": "0.45"}),
    # ⚖️ THE CONTROL, MEASURED AS A CONTROL. Climb the ×1 chain to the top and
    # every bar is still muted — no amber anywhere on the bench. That is the
    # flat line, and it is the evidence that the mechanism is persistence
    # rather than toxicity.
    dict(name="B9 bioaccumulation · the ×1 control reaches the top with no alert",
         on=B9_TOXIC, drive="b9-chem-control",
         sel=".ks3-ba-level:not([data-harmful]) .ks3-ba-bar",
         props={"background-color": "#C6B9A7"}),
    dict(name="B9 bioaccumulation · the control's verdict lands on the same ground",
         on=B9_TOXIC, drive="b9-chem-control",
         sel=".ks3-ba-verdict:not([hidden])",
         props={"background-color": "#FBF3E6", "color": "#221E1B"}),

    # ── b9-06 · quadrat-bench ──
    dict(name="B9 quadrat-bench · a dial label is muted mono on ink",
         on=B9_QUADRAT, sel=".ks3-qb-diallabel",
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "14px"}),
    dict(name="B9 quadrat-bench · the chosen method is the alert ground",
         on=B9_QUADRAT, sel='.ks3-qb-tab[aria-pressed="true"]',
         props={"background-color": "#FFC53D", "color": "#221E1B",
                "min-height": "44px"}),
    dict(name="B9 quadrat-bench · the field is a square grid, capped at 460px",
         on=B9_QUADRAT, sel=".ks3-qb-grid",
         props={"display": "grid", "max-width": "460px"}),
    # ⚖️ AN UNCOUNTED SQUARE IS A FAINT ACCENT WASH WITH NO OUTLINE AND NO
    # NUMBER. The contents are hidden until they are counted or the truth is
    # shown — which is what makes committing to an estimate feel like
    # committing, and what stops the answer being read off the grid.
    dict(name="B9 quadrat-bench · an uncounted square is a faint wash, no outline",
         on=B9_QUADRAT, sel=".ks3-qb-cell",
         props={"background-color": "rgba(228, 87, 46, 0.08)",
                "color": "#FBF3E6", "font-family": "DM Mono",
                "font-size": "12px", "border-top-color": "rgba(0, 0, 0, 0)"}),
    dict(name="B9 quadrat-bench · the grid caption is muted mono in caps",
         on=B9_QUADRAT, sel=".ks3-qb-caption",
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "14px", "text-transform": "uppercase"}),
    dict(name="B9 quadrat-bench · the field sits on the nested dark panel",
         on=B9_QUADRAT, sel=".ks3-qb-panel",
         props={"background-color": "#3E3730"}),
    dict(name="B9 quadrat-bench · the sample button is inverted on ink",
         on=B9_QUADRAT, sel=".ks3-qb-sample",
         props={"background-color": "#FBF3E6", "color": "#221E1B",
                "min-height": "44px"}),
    # ⚖️ THE REVEAL IS LOCKED UNTIL A SAMPLE HAS BEEN TAKEN. Two-stage
    # completion is Design's, and the rail ticks on the SECOND stage: an
    # estimate you can check before you have made one is not a check.
    dict(name="B9 quadrat-bench · the reveal is locked before a sample",
         on=B9_QUADRAT, sel=".ks3-qb-truth[disabled]",
         props={"opacity": "0.45"}),
    dict(name="B9 quadrat-bench · the figures panel arrives as a grid on a well",
         on=B9_QUADRAT, drive="b9-field-sampled",
         sel=".ks3-qb-figures:not([hidden])",
         props={"display": "grid",
                "background-color": "rgba(255, 255, 255, 0.06)"}),
    dict(name="B9 quadrat-bench · a figure's label is muted mono",
         on=B9_QUADRAT, drive="b9-field-sampled", sel=".ks3-qb-figlabel",
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "13px"}),
    dict(name="B9 quadrat-bench · the mean is on-dark display type",
         on=B9_QUADRAT, drive="b9-field-sampled",
         sel='[data-qb-figure="mean"] .ks3-qb-figvalue',
         props={"color": "#FBF3E6", "font-family": "Bricolage Grotesque",
                "font-size": "26px", "font-weight": "800"}),
    dict(name="B9 quadrat-bench · the estimate takes the alert", on=B9_QUADRAT,
         drive="b9-field-sampled",
         sel='[data-qb-figure="estimate"] .ks3-qb-figvalue',
         props={"color": "#FFC53D"}),
    # ⚖️ THE REAL TOTAL IS WITHHELD IN THE SAME SLOT AND THE SAME TYPE, muted
    # rather than absent — so the student can see there IS an answer being held
    # back. An empty slot would read as the bench failing to compute it.
    dict(name="B9 quadrat-bench · the withheld total is muted, not absent",
         on=B9_QUADRAT, drive="b9-field-sampled",
         sel='[data-qb-figure="real"]:not([data-revealed]) .ks3-qb-figvalue',
         props={"color": "#C6B9A7"}),
    dict(name="B9 quadrat-bench · a counted square is outlined on-dark",
         on=B9_QUADRAT, drive="b9-field-sampled",
         sel=".ks3-qb-cell[data-in-sample]",
         props={"border-top-color": "#FBF3E6", "border-top-width": "2px"}),
    # ⊕ MRB-252 (RULED) · audit 3.4 — the sharpest of the six. 26px/800 IS
    # large text and it still measured 2.89:1, because `.ks3-qb-figures` sits
    # on rgba(255,255,255,.06) over the dark panel and composites to #4A433C,
    # one step lighter than the ground `--ks3-ok` was ever rated on. That is
    # the whole argument for a token measured against the tile: this row would
    # have passed a naive re-derivation done against #3E3730.
    dict(name="B9 quadrat-bench · the revealed total turns green", on=B9_QUADRAT,
         drive="b9-field-revealed",
         sel='[data-qb-figure="real"][data-revealed] .ks3-qb-figvalue',
         props={"color": "#40DD84"}),
    dict(name="B9 quadrat-bench · the verdict is the page ground on ink",
         on=B9_QUADRAT, drive="b9-field-revealed",
         sel=".ks3-qb-verdict:not([hidden])",
         props={"background-color": "#FBF3E6", "color": "#221E1B",
                "font-size": "18px"}),
    # ═══ END B9 ═══ rows

    # ═══ BEGIN B10 ═══ rows
    # ⚠️ THESE ROWS EXIST BECAUSE B8 SHIPPED WITHOUT THEM and B9 was the
    # correction. A dispatch entry is not a component (contract §6.6); a green
    # kinds gate over an unmeasured instrument says nothing at all. Every B10
    # instrument below carries a full state sweep: resting, chosen, gated,
    # revealed, spent — and every state the science depends on.
    #
    # ⚠️ AND THEY ARE AIMED AT THE SPECIFICITY TRAP. All five B10 instruments
    # sit on `ks3-dark`. `.ks3-dark p` is (0,1,1) and beats a bare instrument
    # class at (0,1,0) — so a rule written as `.ks3-vp-axis { color: … }` LOSES
    # to the dark-ground default and ships a caption at roughly 1.2:1 that no
    # grep will ever find, because the CSS is right there saying the correct
    # thing. Every row below is asserted against the element as the BROWSER
    # resolves it, not as the stylesheet declares it.

    # ── b10-01 · variation-plotter ──
    dict(name="B10 variation-plotter · the characteristic label is muted mono",
         on=B10_PLOT, sel=".ks3-vp-tabslabel",
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "14px"}),
    # ⚖️ A CHOSEN TAB IS THE ALERT GROUND, which is Design's own `seg()` and
    # NOT the platform's alert border. Still not a mark: it says "this is the
    # characteristic on the bench", never "this is correct".
    dict(name="B10 variation-plotter · the chosen characteristic is the alert ground",
         on=B10_PLOT, sel='.ks3-vp-tab[aria-pressed="true"]',
         props={"background-color": "#FFC53D", "color": "#221E1B",
                "min-height": "44px"}),
    dict(name="B10 variation-plotter · an unchosen characteristic stays on the panel ground",
         on=B10_PLOT, sel='.ks3-vp-tab[aria-pressed="false"]',
         props={"background-color": "#3E3730", "color": "#FBF3E6"}),
    dict(name="B10 variation-plotter · the bench sits on the nested dark panel",
         on=B10_PLOT, sel=".ks3-vp-panel",
         props={"background-color": "#3E3730"}),
    dict(name="B10 variation-plotter · the characteristic name is on-dark at 20px",
         on=B10_PLOT,
         sel="[data-vp-charpanel]:not([hidden]) .ks3-vp-name",
         props={"color": "#FBF3E6", "font-size": "20px",
                "font-weight": "700"}),
    dict(name="B10 variation-plotter · the predict ask is on-dark, not muted",
         on=B10_PLOT,
         sel="[data-vp-charpanel]:not([hidden]) .ks3-vp-predictlabel",
         props={"color": "#FBF3E6", "font-size": "17px"}),
    dict(name="B10 variation-plotter · a predict button clears the tap target",
         on=B10_PLOT,
         sel="[data-vp-charpanel]:not([hidden]) .ks3-vp-pred",
         props={"min-height": "44px", "font-size": "16px"}),
    # ⚖️ THE PLOT BUTTON IS DISABLED ON THE RESTING PAGE, and dimmed so the
    # student can see there IS a control being withheld. This is Law 4 drawn:
    # the graph cannot be reached before a shape has been committed to.
    dict(name="B10 variation-plotter · the plot button is dimmed until a shape is committed",
         on=B10_PLOT, sel=".ks3-vp-plot[disabled]",
         props={"opacity": "0.45"}),
    dict(name="B10 variation-plotter · the plot button is inverted on ink",
         on=B10_PLOT, sel=".ks3-vp-plot",
         props={"background-color": "#FBF3E6", "color": "#221E1B",
                "min-height": "44px"}),
    # ── driven: one characteristic predicted and plotted ──
    dict(name="B10 variation-plotter · the chosen prediction takes the alert ground",
         on=B10_PLOT, drive="b10-plot-run",
         sel='[data-vp-charpanel]:not([hidden]) .ks3-vp-pred[aria-pressed="true"]',
         props={"background-color": "#FFC53D", "color": "#221E1B"}),
    # ⚖️⚖️ THE GAP IS THE LESSON, and it is asserted on PAINTED GEOMETRY inside
    # `b10-plot-both`, not here. A continuous characteristic's bars fill their
    # column and MEET; a discontinuous one's are 6px narrower and stand apart.
    # Neither width is a fixed number — the column is `flex: 1 1 0` and a
    # six-bin chart's column is not a seven-bin chart's — so the claim is
    # "the bar is exactly as wide as its column" and "the bar is exactly 6px
    # narrower", which is a relation between two measurements and not a value
    # a `props` row can hold. If the discontinuous rule ever resolves to the
    # full column width the bench is drawing a histogram of blood groups and
    # telling a student that is what one looks like; nothing else in the build
    # would notice.
    dict(name="B10 variation-plotter · the bars are drawn to the derived gap",
         on=B10_PLOT, drive="b10-plot-both",
         sel="[data-vp-charpanel]:not([hidden]) .ks3-vp-col",
         props={"min-width": "0px"}),
    dict(name="B10 variation-plotter · the bar is the alert fill",
         on=B10_PLOT, drive="b10-plot-run",
         sel="[data-vp-charpanel]:not([hidden]) .ks3-vp-bar",
         props={"background-color": "#FFC53D"}),
    dict(name="B10 variation-plotter · the chart sits in a translucent well",
         on=B10_PLOT, drive="b10-plot-run",
         sel="[data-vp-charpanel]:not([hidden]) .ks3-vp-chart",
         props={"height": "170px",
                "background-color": "rgba(255, 255, 255, 0.06)"}),
    dict(name="B10 variation-plotter · the bin count is muted mono at 12px",
         on=B10_PLOT, drive="b10-plot-run",
         sel="[data-vp-charpanel]:not([hidden]) .ks3-vp-n",
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "12px"}),
    dict(name="B10 variation-plotter · the bin label is muted mono at 11px",
         on=B10_PLOT, drive="b10-plot-run",
         sel="[data-vp-charpanel]:not([hidden]) .ks3-vp-binlabel",
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "11px"}),
    dict(name="B10 variation-plotter · the axis caption is muted mono, uppercase",
         on=B10_PLOT, drive="b10-plot-run",
         sel="[data-vp-charpanel]:not([hidden]) .ks3-vp-axis",
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "14px", "text-transform": "uppercase"}),
    # ⚖️ THE VERDICT IS THE PAGE GROUND ON AN INK BLOCK — cream inside ink,
    # which is the one place in this instrument where the text has to be INK
    # and not on-dark. It is the element the whole commitment exists to reach.
    dict(name="B10 variation-plotter · the verdict is the page ground on an ink block",
         on=B10_PLOT, drive="b10-plot-run",
         sel="[data-vp-charpanel]:not([hidden]) .ks3-vp-verdict",
         props={"background-color": "#FBF3E6", "color": "#221E1B"}),
    # ⛔ ACCENT-TEXT AT 6.0:1, NEVER `--ks3-accent` AT 3.4:1. The tag is 14px
    # mono, which is small text, and it is ONE TONE for both verdicts — a
    # bench says whether the prediction held, in words, and says it the same
    # way whichever way it went (schema §0.6). Green for right and red for
    # wrong would make a bench into a marker, which only the ladder is.
    dict(name="B10 variation-plotter · the verdict tag is accent-TEXT mono, never accent",
         on=B10_PLOT, drive="b10-plot-run",
         sel="[data-vp-charpanel]:not([hidden]) .ks3-vp-tag:not([hidden])",
         props={"color": "#A93411", "font-family": "DM Mono",
                "font-size": "14px"}),
    dict(name="B10 variation-plotter · the kind line is display 800 at 22px",
         on=B10_PLOT, drive="b10-plot-run",
         sel="[data-vp-charpanel]:not([hidden]) .ks3-vp-kind",
         props={"color": "#221E1B", "font-weight": "800",
                "font-size": "22px"}),
    dict(name="B10 variation-plotter · the shape answer reads in ink body",
         on=B10_PLOT, drive="b10-plot-run",
         sel="[data-vp-charpanel]:not([hidden]) .ks3-vp-shape",
         props={"color": "#3B342E", "font-size": "18px"}),
    # ⚖️⚖️ SHAPE AND CAUSE ARE TWO QUESTIONS AND THE RULE IS THE LINE BETWEEN
    # THEM. `#s-think`'s whole confrontation is that a smooth curve says
    # nothing about the cause; a merge of these two paragraphs would delete the
    # lesson's second half while leaving every word of it on the page.
    dict(name="B10 variation-plotter · the cause answer is divided off by a rule",
         on=B10_PLOT, drive="b10-plot-run",
         sel="[data-vp-charpanel]:not([hidden]) .ks3-vp-cause",
         props={"color": "#3B342E", "font-size": "18px",
                "border-top-color": "#E0D2B9", "border-top-width": "2px"}),
    dict(name="B10 variation-plotter · the spent plot button dims",
         on=B10_PLOT, drive="b10-plot-run",
         sel=".ks3-vp-plot[disabled]",
         props={"opacity": "0.45"}),

    # ── b10-02 · zoom-bench ──
    dict(name="B10 zoom-bench · the ladder sits on the nested dark panel",
         on=B10_ZOOM, sel=".ks3-zb-panel",
         props={"background-color": "#3E3730"}),
    # ⚖️⚖️ AN UNREACHED LEVEL IS DIMMED AND STILL DRAWN, and this is the row
    # that says so. The whole ladder is on screen from the first paint so the
    # SCALE COLUMN can be read as a column — that column is the lesson's
    # argument. If this ever resolves to 1 the bench has given away every body
    # paragraph before the first press; if the row is hidden instead, the
    # column stops existing and six levels become six facts in a list.
    dict(name="B10 zoom-bench · an unreached level dims and takes no outline",
         on=B10_ZOOM, sel=".ks3-zb-level:not([data-shown])",
         props={"opacity": "0.8", "border-top-color": "rgba(0, 0, 0, 0)"}),
    dict(name="B10 zoom-bench · an unreached level's name is muted",
         on=B10_ZOOM, sel=".ks3-zb-level:not([data-shown]) .ks3-zb-name",
         props={"color": "#C6B9A7", "font-size": "19px",
                "font-weight": "700"}),
    dict(name="B10 zoom-bench · a reached level's name is on-dark headline",
         on=B10_ZOOM, sel=".ks3-zb-level[data-shown] .ks3-zb-name",
         props={"color": "#FBF3E6", "font-size": "19px",
                "font-weight": "700"}),
    # ⚖️⚖️ THE SCALE FIGURE IS THE ALERT ON EVERY ROW, REACHED OR NOT. It is
    # the column the lesson is about — 1.6 m down to 0.0000003 mm apart — and
    # dimming it per row would leave the journey unreadable before it starts.
    # The row's own 45% is what says "not yet"; a second treatment on the
    # figure would say "not important".
    dict(name="B10 zoom-bench · the scale figure is alert mono on every row",
         on=B10_ZOOM, sel=".ks3-zb-level:not([data-shown]) .ks3-zb-scale",
         props={"color": "#FFC53D", "font-family": "DM Mono",
                "font-size": "15px"}),
    # ⊕ MRB-257 · audit 3.13 — same wash, same repair. .06 = #4A433C.
    dict(name="B10 zoom-bench · the level just reached takes the alert outline",
         on=B10_ZOOM, sel=".ks3-zb-level[data-here]",
         props={"border-top-color": "#FFC53D", "border-top-width": "2px",
                "background-color": "rgba(255, 255, 255, 0.06)"}),
    dict(name="B10 zoom-bench · a reached level's number is the alert chip",
         on=B10_ZOOM, sel=".ks3-zb-level[data-shown] .ks3-zb-num",
         props={"background-color": "#FFC53D", "color": "#221E1B",
                "width": "30px", "height": "30px"}),
    dict(name="B10 zoom-bench · an unreached number is a muted outline",
         on=B10_ZOOM, sel=".ks3-zb-level:not([data-shown]) .ks3-zb-num",
         props={"background-color": "rgba(0, 0, 0, 0)", "color": "#C6B9A7",
                "border-top-color": "#C6B9A7"}),
    dict(name="B10 zoom-bench · a revealed level body reads in on-dark body",
         on=B10_ZOOM, sel=".ks3-zb-level[data-shown] .ks3-zb-body",
         props={"color": "#E7DECE", "font-size": "18px"}),
    dict(name="B10 zoom-bench · the zoom button is inverted on ink",
         on=B10_ZOOM, sel=".ks3-zb-in",
         props={"background-color": "#FBF3E6", "color": "#221E1B",
                "min-height": "44px"}),
    dict(name="B10 zoom-bench · the back-out button is inverted on ink",
         on=B10_ZOOM, sel=".ks3-zb-out",
         props={"background-color": "#FBF3E6", "color": "#221E1B",
                "min-height": "44px"}),
    # ⚠️ THE SAY-IT-BACK PANEL IS PART OF THE BENCH, not a block of its own —
    # measured, inside `<section id="s-bench">`. Its own translucent ground is
    # what tells the eye it is a second thing on the same bench.
    dict(name="B10 zoom-bench · the say-it-back panel is a well on the ink block",
         on=B10_ZOOM, sel=".ks3-zb-say",
         props={"background-color": "rgba(255, 255, 255, 0.06)"}),
    dict(name="B10 zoom-bench · the say-it-back label is muted mono, uppercase",
         on=B10_ZOOM, sel=".ks3-zb-saylabel",
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "14px", "text-transform": "uppercase"}),
    # ⛔ A PRESSED QUESTION TAB SAYS WHICH QUESTION IS BEING LOOKED AT, and
    # nothing else. This panel gates nothing and marks nothing: every answer is
    # visible the moment its question is chosen, and there is no right one.
    dict(name="B10 zoom-bench · the chosen question is the alert ground",
         on=B10_ZOOM, sel='.ks3-zb-qtab[aria-pressed="true"]',
         props={"background-color": "#FFC53D", "color": "#221E1B",
                "min-height": "44px"}),
    dict(name="B10 zoom-bench · an unchosen question stays on the panel ground",
         on=B10_ZOOM, sel='.ks3-zb-qtab[aria-pressed="false"]',
         props={"background-color": "#3E3730", "color": "#FBF3E6"}),
    dict(name="B10 zoom-bench · the answer reads in on-dark body",
         on=B10_ZOOM, sel="[data-zb-answer]:not([hidden])",
         props={"color": "#E7DECE", "font-size": "18px"}),
    # ── driven: all six levels open ──
    dict(name="B10 zoom-bench · the spent zoom button dims",
         on=B10_ZOOM, drive="b10-zoom-bottomed", sel=".ks3-zb-in[disabled]",
         props={"opacity": "0.45"}),
    # ⚖️ THE BOTTOM-OUT PARAGRAPH IS THE PAGE GROUND ON AN INK BLOCK — cream
    # inside ink, the one element on this bench whose text is INK. It is the
    # sentence that says nothing was swapped for anything else on the way down,
    # which is the whole of `#s-think` on this page.
    dict(name="B10 zoom-bench · the close is the page ground on an ink block",
         on=B10_ZOOM, drive="b10-zoom-bottomed",
         sel=".ks3-zb-close:not([hidden])",
         props={"background-color": "#FBF3E6", "color": "#221E1B",
                "font-size": "18px"}),
    dict(name="B10 zoom-bench · the last level is the one lit at the bottom",
         on=B10_ZOOM, drive="b10-zoom-bottomed",
         sel=".ks3-zb-level[data-here] .ks3-zb-num",
         props={"background-color": "#FFC53D", "color": "#221E1B"}),

    # ── the accent BADGE, drawn on two pages at two sizes (⊕ MRB-248) ──
    # ⚠️ REGISTERED BECAUSE THE KEYS WERE DEAD WITHOUT IT. b10-03 authored
    # `initials` and b10-04 authored `num`, `_rule_card` read neither, and
    # under contract R5 an authored key with no read site fails the audit —
    # while the page looked entirely deliberate, because the cards still
    # rendered their other parts. Same shape as MRB-245's ten empty cards, one
    # slot smaller.
    dict(name="badged card is one column of full-width rows, not the auto grid",
         on=B10_MODEL, sel=".ks3-rule-cards[data-badged]",
         props={"display": "flex", "flex-direction": "column"}),
    dict(name="badged card is a two-column grid", on=B10_MODEL,
         sel=".ks3-rule-cards > li[data-badge]",
         props={"display": "grid"}),
    # ⊕ MRB-257 · audit 3.13 — the second row that pinned cream on the accent.
    # 16px/800 is body size; the token says "LARGE TEXT ONLY. Never body size",
    # and cream on it is 3.34:1. Ink is 4.49:1 and the fill does not move.
    dict(name="initials badge is a 44px accent square", on=B10_MODEL,
         sel='.ks3-rule-badge[data-badge="initials"]',
         props={"width": "44px", "height": "44px",
                "background-color": "#E4572E", "color": "#221E1B",
                "font-size": "16px"}),
    # ⚠️ ON A BADGED CARD THE NAME IS THE HEADLINE AND THE ROLE SITS UNDER IT,
    # which is the reverse of a b1-04 card. The badge already does the
    # labelling the role line does there, so promoting the role would give the
    # card a laboratory for a title and a person for a subtitle.
    dict(name="badged card's name is display 800 at 22px", on=B10_MODEL,
         sel=".ks3-rule-cards > li[data-badge] > .ks3-rule-term",
         props={"font-family": "Bricolage Grotesque", "font-weight": "800",
                "font-size": "22px"}),
    # ⊕ MRB-248 / B11 — the card's FOURTH part. `.ks3-rule-eg` is mono at 15px,
    # which is right for "shrew · dormouse · hedgehog" and wrong for two
    # sentences of prose, so what a method cannot do gets a slot of its own at
    # 17px in ink-muted — Design's own treatment, measured off b11-04 line 161.
    # ⚠️ REPOINTED 18 Aug 2026. This row was written parked, and a parked row's
    # `on` is never exercised — so it sat on `LESSON` (the rebuilt c1-04, which
    # authors no rule cards at all) and nobody could tell. Un-parking it is what
    # surfaced that: the gate reported the component registered and not
    # rendered, which was true of the page it named and false of the key stage.
    # A parked row's page is a claim nothing checks; check it when you un-park.
    dict(name="card limit is muted prose, not the mono example line",
         on=B11_BLIGHT, sel=".ks3-rule-limit",
         props={"font-size": "17px", "color": "#5F564F"}),
    dict(name="badged card's role is accent-TEXT mono under the name",
         on=B10_MODEL,
         sel=".ks3-rule-cards > li[data-badge] > .ks3-rule-role",
         props={"color": "#A93411", "font-family": "DM Mono",
                "font-size": "14px"}),

    # ── b10-03 · model-builder ──
    dict(name="B10 model-builder · the dial name is muted mono, uppercase",
         on=B10_MODEL, sel=".ks3-dh-dialname",
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "14px", "text-transform": "uppercase"}),
    # ⛔ A PRESSED DIAL IS THE ALERT GROUND AND IT IS NOT A MARK. It says "this
    # is the model on the bench" — the bench opens on PAULING'S WRONG MODEL
    # with all three dials pressed, so a dial that read as a verdict would open
    # by telling the student their model was right.
    dict(name="B10 model-builder · the chosen dial is the alert ground",
         on=B10_MODEL, sel='.ks3-dh-opt[aria-pressed="true"]',
         props={"background-color": "#FFC53D", "color": "#221E1B",
                "min-height": "44px"}),
    dict(name="B10 model-builder · an unchosen dial stays on the panel ground",
         on=B10_MODEL, sel='.ks3-dh-opt[aria-pressed="false"]',
         props={"background-color": "#3E3730", "color": "#FBF3E6"}),
    dict(name="B10 model-builder · the bench sits on the nested dark panel",
         on=B10_MODEL, sel=".ks3-dh-panel",
         props={"background-color": "#3E3730"}),
    dict(name="B10 model-builder · the model line is on-dark at 20px",
         on=B10_MODEL, sel=".ks3-dh-modelline",
         props={"color": "#FBF3E6", "font-size": "20px",
                "font-weight": "700"}),
    dict(name="B10 model-builder · an evidence card sits in a translucent well",
         on=B10_MODEL, sel=".ks3-dh-card",
         props={"background-color": "rgba(255, 255, 255, 0.06)"}),
    # ⚖️⚖️ THE CARD OUTLINE IS THE VERDICT AND IT IS ON THE MODEL, NOT ON THE
    # STUDENT. One of the three B10 benches that adjudicate a commitment
    # (schema §0.6), shipped as Design drew it: green when the evidence is
    # consistent with the model, alert when it rules that model out. These two
    # rows are what stop the treatment migrating onto a dial button.
    dict(name="B10 model-builder · a failing card takes the alert outline",
         on=B10_MODEL, sel=".ks3-dh-card:not([data-pass])",
         props={"border-top-color": "#FFC53D", "border-top-width": "2px"}),
    dict(name="B10 model-builder · a failing card's verdict is alert mono",
         on=B10_MODEL,
         sel='.ks3-dh-card:not([data-pass]) [data-dh-tag="fail"]',
         props={"color": "#FFC53D", "font-family": "DM Mono",
                "font-size": "14px", "text-transform": "uppercase"}),
    dict(name="B10 model-builder · the evidence name is on-dark at 18px",
         on=B10_MODEL, sel=".ks3-dh-cardname",
         props={"color": "#FBF3E6", "font-size": "18px",
                "font-weight": "700"}),
    dict(name="B10 model-builder · what the evidence IS reads in on-dark body",
         on=B10_MODEL, sel=".ks3-dh-what",
         props={"color": "#E7DECE", "font-size": "17px"}),
    # ⚖️ THE ELIMINATION TEXT IS AMBER, AND AMBER IS A WRONG IDEA BEING
    # CONFRONTED. It is the only line on the bench that tells a student which
    # decision to change, and it is about the MODEL.
    dict(name="B10 model-builder · the elimination line is amber",
         on=B10_MODEL, sel=".ks3-dh-card:not([data-pass]) .ks3-dh-why",
         props={"color": "#FFC53D", "font-size": "17px"}),
    dict(name="B10 model-builder · the verdict is the page ground on an ink block",
         on=B10_MODEL, sel=".ks3-dh-verdict",
         props={"background-color": "#FBF3E6", "color": "#221E1B"}),
    dict(name="B10 model-builder · the verdict tag is accent-TEXT mono, never accent",
         on=B10_MODEL, sel=".ks3-dh-verdicttag",
         props={"color": "#A93411", "font-family": "DM Mono",
                "font-size": "14px"}),
    dict(name="B10 model-builder · the verdict body reads in ink body",
         on=B10_MODEL, sel=".ks3-dh-verdictbody",
         props={"color": "#3B342E", "font-size": "18px"}),
    # ── driven: the double helix built ──
    dict(name="B10 model-builder · a passing card takes the green outline",
         on=B10_MODEL, drive="b10-model-solved",
         sel=".ks3-dh-card[data-pass]",
         props={"border-top-color": "#12A150", "border-top-width": "2px"}),
    # ⊕ MRB-252 (RULED) · audit 3.4 — 14px mono is text. The card OUTLINE in
    # the row above stays #12A150 and is meant to: an outline is a mark, and
    # the ruling narrows the token to marks and fills rather than retiring it.
    # The two rows sitting next to each other is the ruling, legible.
    dict(name="B10 model-builder · a passing card's verdict is green mono",
         on=B10_MODEL, drive="b10-model-solved",
         sel='.ks3-dh-card[data-pass] [data-dh-tag="pass"]:not([hidden])',
         props={"color": "#40DD84", "font-family": "DM Mono",
                "font-size": "14px"}),

    # ── b10-04 · pea-cross ──
    dict(name="B10 pea-cross · the parent name is muted mono, uppercase",
         on=B10_CROSS, sel=".ks3-pc-parentname",
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "14px", "text-transform": "uppercase"}),
    dict(name="B10 pea-cross · the chosen genotype is the alert ground",
         on=B10_CROSS, sel='.ks3-pc-geno[aria-pressed="true"]',
         props={"background-color": "#FFC53D", "color": "#221E1B",
                "min-height": "44px"}),
    dict(name="B10 pea-cross · an unchosen genotype stays on the panel ground",
         on=B10_CROSS, sel='.ks3-pc-geno[aria-pressed="false"]',
         props={"background-color": "#3E3730", "color": "#FBF3E6"}),
    dict(name="B10 pea-cross · the plot sits on the nested dark panel",
         on=B10_CROSS, sel=".ks3-pc-panel",
         props={"background-color": "#3E3730"}),
    dict(name="B10 pea-cross · the cross line is on-dark at 20px",
         on=B10_CROSS, sel=".ks3-pc-crossline",
         props={"color": "#FBF3E6", "font-size": "20px",
                "font-weight": "700"}),
    dict(name="B10 pea-cross · the note reads in on-dark body on a well",
         on=B10_CROSS, sel="[data-pc-note]:not([hidden])",
         props={"color": "#E7DECE", "font-size": "18px",
                "background-color": "rgba(255, 255, 255, 0.06)"}),
    dict(name="B10 pea-cross · the grow buttons are inverted on ink",
         on=B10_CROSS, sel=".ks3-pc-one",
         props={"background-color": "#FBF3E6", "color": "#221E1B",
                "min-height": "44px"}),
    dict(name="B10 pea-cross · the clear button is inverted on ink",
         on=B10_CROSS, sel=".ks3-pc-clear",
         props={"background-color": "#FBF3E6", "color": "#221E1B",
                "min-height": "44px"}),
    # ── driven: one seed grown ──
    dict(name="B10 pea-cross · the most-recent-seed card is a well",
         on=B10_CROSS, drive="b10-cross-grown",
         sel="[data-pc-last]:not([hidden])",
         props={"background-color": "rgba(255, 255, 255, 0.06)"}),
    dict(name="B10 pea-cross · the seed label is muted mono, uppercase",
         on=B10_CROSS, drive="b10-cross-grown", sel=".ks3-pc-lastlabel",
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "14px", "text-transform": "uppercase"}),
    dict(name="B10 pea-cross · the seed line reads in on-dark body",
         on=B10_CROSS, drive="b10-cross-grown", sel=".ks3-pc-lastline",
         props={"color": "#E7DECE", "font-size": "19px"}),
    dict(name="B10 pea-cross · the tally name is on-dark at 17px",
         on=B10_CROSS, drive="b10-cross-grown", sel=".ks3-pc-rowname",
         props={"color": "#FBF3E6", "font-size": "17px"}),
    dict(name="B10 pea-cross · the tally figure is muted mono",
         on=B10_CROSS, drive="b10-cross-grown", sel="[data-pc-value]",
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "16px"}),
    # ⚖️ TWO BARS, TWO COLOURS, AND NEITHER IS A MARK. Purple-flowered takes
    # the alert and white-flowered the muted — a quantity distinguished from
    # another quantity, not a right answer from a wrong one. There is nothing
    # on this bench to be right about: chance decides each seed.
    dict(name="B10 pea-cross · the purple bar is the alert fill",
         on=B10_CROSS, drive="b10-cross-grown",
         sel='.ks3-pc-row[data-pc-row="dominant"] .ks3-pc-bar',
         props={"background-color": "#FFC53D"}),
    dict(name="B10 pea-cross · the white bar is the muted fill, not a second alert",
         on=B10_CROSS, drive="b10-cross-grown",
         sel='.ks3-pc-row[data-pc-row="recessive"] .ks3-pc-bar',
         props={"background-color": "#C6B9A7"}),
    dict(name="B10 pea-cross · the bars sit in a translucent well",
         on=B10_CROSS, drive="b10-cross-grown", sel=".ks3-pc-track",
         props={"height": "16px",
                "background-color": "rgba(255, 255, 255, 0.08)"}),
    dict(name="B10 pea-cross · the ratio line is alert mono",
         on=B10_CROSS, drive="b10-cross-grown", sel="[data-pc-ratio]",
         props={"color": "#FFC53D", "font-family": "DM Mono",
                "font-size": "16px"}),

    # ── b10-05 · species-cases ──
    dict(name="B10 species-cases · the case label is muted mono, uppercase",
         on=B10_SPECIES, sel=".ks3-sc-tabslabel",
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "14px", "text-transform": "uppercase"}),
    dict(name="B10 species-cases · the chosen case is the alert ground",
         on=B10_SPECIES, sel='.ks3-sc-tab[aria-pressed="true"]',
         props={"background-color": "#FFC53D", "color": "#221E1B",
                "min-height": "44px"}),
    dict(name="B10 species-cases · the bench sits on the nested dark panel",
         on=B10_SPECIES, sel=".ks3-sc-panel",
         props={"background-color": "#3E3730"}),
    dict(name="B10 species-cases · the case title is display 800 at 25px",
         on=B10_SPECIES, sel="[data-sc-panel]:not([hidden]) .ks3-sc-title",
         props={"color": "#FBF3E6", "font-family": "Bricolage Grotesque",
                "font-weight": "800", "font-size": "25px"}),
    dict(name="B10 species-cases · the facts read in on-dark body",
         on=B10_SPECIES, sel="[data-sc-panel]:not([hidden]) .ks3-sc-facts",
         props={"color": "#E7DECE", "font-size": "18px"}),
    # ⚖️ A VERDICT IS A FULL-WIDTH ROW ON THE PANEL GROUND, not a segment.
    # Three sentences that have to be READ — one of them is "the test does not
    # settle it", which is the whole instrument — and a chip row would invite
    # them to be scanned.
    dict(name="B10 species-cases · a verdict is a full-width row, not a segment",
         on=B10_SPECIES,
         sel='[data-sc-panel]:not([hidden]) .ks3-sc-verdict[aria-pressed="false"]',
         props={"background-color": "rgba(0, 0, 0, 0)", "color": "#FBF3E6",
                "font-size": "18px", "min-height": "44px"}),
    dict(name="B10 species-cases · the verdict letter is a drawn ring, not a tint",
         on=B10_SPECIES, sel="[data-sc-panel]:not([hidden]) .ks3-sc-letter",
         props={"width": "26px", "height": "26px", "color": "#C6B9A7",
                "border-top-color": "#C6B9A7"}),
    dict(name="B10 species-cases · the check button is dimmed until a verdict is chosen",
         on=B10_SPECIES, sel=".ks3-sc-check[disabled]",
         props={"opacity": "0.45"}),
    dict(name="B10 species-cases · the tally beside it is muted mono",
         on=B10_SPECIES, sel="[data-sc-tally]",
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "15px"}),
    # ── driven: one case committed and checked ──
    dict(name="B10 species-cases · the chosen verdict takes the alert outline",
         on=B10_SPECIES, drive="b10-species-checked",
         sel='[data-sc-panel]:not([hidden]) .ks3-sc-verdict[aria-pressed="true"]',
         props={"border-top-color": "#FFC53D", "border-top-width": "2px",
                "background-color": "rgba(255, 255, 255, 0.1)"}),
    # ⛔ AND THE UNCHOSEN VERDICTS DIM RATHER THAN BEING MARKED. No green on
    # the right one, no red on the wrong one, no badge — the bench says whether
    # the commitment held in WORDS on the cream panel (schema §0.6) and the
    # student's own button is never marked (MRB-196 R10).
    dict(name="B10 species-cases · a spent unchosen verdict dims and takes no mark",
         on=B10_SPECIES, drive="b10-species-checked",
         sel=('[data-sc-panel]:not([hidden])[data-sc-opened] '
              '.ks3-sc-verdict[aria-pressed="false"]'),
         props={"opacity": "0.5", "background-color": "rgba(0, 0, 0, 0)"}),
    dict(name="B10 species-cases · the outcome is the page ground on an ink block",
         on=B10_SPECIES, drive="b10-species-checked",
         sel="[data-sc-panel]:not([hidden]) [data-sc-out]:not([hidden])",
         props={"background-color": "#FBF3E6", "color": "#221E1B"}),
    dict(name="B10 species-cases · the outcome tag is accent-TEXT mono, never accent",
         on=B10_SPECIES, drive="b10-species-checked",
         sel="[data-sc-panel]:not([hidden]) .ks3-sc-tag:not([hidden])",
         props={"color": "#A93411", "font-family": "DM Mono",
                "font-size": "14px"}),
    dict(name="B10 species-cases · the answer is display 800 at 22px",
         on=B10_SPECIES, drive="b10-species-checked",
         sel="[data-sc-panel]:not([hidden]) .ks3-sc-answer",
         props={"color": "#221E1B", "font-family": "Bricolage Grotesque",
                "font-weight": "800", "font-size": "22px"}),
    dict(name="B10 species-cases · the reasoning reads in ink body",
         on=B10_SPECIES, drive="b10-species-checked",
         sel="[data-sc-panel]:not([hidden]) .ks3-sc-why",
         props={"color": "#3B342E", "font-size": "18px"}),
    dict(name="B10 species-cases · the spent check button dims",
         on=B10_SPECIES, drive="b10-species-checked",
         sel=".ks3-sc-check[disabled]",
         props={"opacity": "0.45"}),
    # ═══ END B10 ═══ rows
    # ═══ BEGIN B11 ═══ rows
    # ⚠️ THE SAME AIM AS B10's BLOCK ABOVE: a dispatch entry is not a component
    # (contract §6.6), and every one of these is asserted against the element
    # as the BROWSER resolves it. All four B11 instruments sit on `ks3-dark`,
    # where `.ks3-dark p` at (0,1,1) beats a bare instrument class at (0,1,0) —
    # so a rule written without the `.ks3-dark` scope ships a sentence at
    # roughly 1.2:1 that no grep will find, because the CSS is right there
    # saying the correct thing.

    # ── b11-01 · advantage-bench ──
    dict(name="B11 advantage-bench · the conditions label is muted mono",
         on=B11_ADV, sel=".ks3-ab-tabslabel",
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "14px", "text-transform": "uppercase"}),
    # ⚖️ A CHOSEN CONDITION IS THE ALERT GROUND, which is Design's own `seg()`
    # and NOT the platform's alert border. Still not a mark: it says "this is
    # the world the bench is standing in", never "this is correct".
    dict(name="B11 advantage-bench · the chosen condition is the alert ground",
         on=B11_ADV, sel='.ks3-ab-tab[aria-pressed="true"]',
         props={"background-color": "#FFC53D", "color": "#221E1B",
                "min-height": "44px"}),
    # ⚖️ AN UNCHOSEN TAB IS THE PANEL GROUND, NOT TRANSPARENT — the platform's
    # `.ks3-dark .ks3-option` against Design's `seg(false)`, which paints
    # `background: transparent`. The platform wins on all five B10 benches and
    # is what shipped there; B11 matching it keeps one control looking like one
    # control across nine pages, which is worth more than a per-unit fidelity
    # to a value Design's own delivered pages disagree with the platform about.
    # Recorded as measured, not as drawn — the drift is B10's, settled, and
    # named here rather than re-argued.
    dict(name="B11 advantage-bench · an unchosen condition stays on the block ground",
         on=B11_ADV, sel='.ks3-ab-tab[aria-pressed="false"]',
         props={"background-color": "#3E3730", "color": "#FBF3E6"}),
    dict(name="B11 advantage-bench · the bench sits on the nested dark panel",
         on=B11_ADV, sel=".ks3-ab-panel",
         props={"background-color": "#3E3730"}),
    dict(name="B11 advantage-bench · the condition headline is on-dark at 20px",
         on=B11_ADV, sel="[data-ab-envpanel]:not([hidden]) .ks3-ab-envname",
         props={"color": "#FBF3E6", "font-size": "20px",
                "font-weight": "700"}),
    dict(name="B11 advantage-bench · what the condition does is muted, not body",
         on=B11_ADV, sel="[data-ab-envpanel]:not([hidden]) .ks3-ab-envnote",
         props={"color": "#C6B9A7", "font-size": "18px"}),
    dict(name="B11 advantage-bench · the variation's name is on-dark at 18px",
         on=B11_ADV, sel="[data-ab-envpanel]:not([hidden]) .ks3-ab-name",
         props={"color": "#FBF3E6", "font-size": "18px",
                "font-weight": "700"}),
    # ⚖️ THE TRACK IS THE 100% THE BAR IS A FRACTION OF, so it is drawn whether
    # the bar fills it or not — a 20% row has to READ as a fifth of something.
    dict(name="B11 advantage-bench · the survival bar runs in a drawn track",
         on=B11_ADV, sel="[data-ab-envpanel]:not([hidden]) .ks3-ab-track",
         props={"height": "16px",
                "background-color": "rgba(255, 255, 255, 0.08)"}),
    # ⚑ AMBER AND GREEN ARE DATA ON THIS BENCH, NOT A MARK. The student has
    # predicted nothing here; amber is the bottom of a column and green is the
    # top of one. Both carry the WORD as well as the colour (" · best here",
    # " · worst here") so nothing is signalled by colour alone (R2). Recorded
    # as values rather than described, so the day the palette question is ruled
    # the gate names them.
    dict(name="B11 advantage-bench · the column's best is green and says so",
         on=B11_ADV,
         sel='[data-ab-envpanel]:not([hidden]) .ks3-ab-chance[data-ab-rank="best"]',
         props={"color": "#40DD84", "font-family": "DM Mono",
                "font-size": "16px"}),
    # ⊕ MRB-252 (RULED) · the amber half. This row's own comment above said
    # the two colours were DATA and asked for the ruling; the ruling agrees
    # that they are data and takes amber away from that job — amber warns, it
    # never merely labels. The bottom of a column is a category, so it is
    # `--ks3-data`. The BARS below follow the same split as the greens: the
    # figure is text and takes the text token, the bar is a fill.
    dict(name="B11 advantage-bench · the column's worst is the data colour and says so",
         on=B11_ADV,
         sel='[data-ab-envpanel]:not([hidden]) .ks3-ab-chance[data-ab-rank="worst"]',
         props={"color": "#8FB7FF", "font-family": "DM Mono",
                "font-size": "16px"}),
    # ⊕ NEW under MRB-252 — the two ranked BARS were never registered at all,
    # so the re-point could have moved the figure and left the bar amber and
    # nothing would have said so. Both ends of the encoding, now.
    dict(name="B11 advantage-bench · the best bar is the mark green fill",
         on=B11_ADV,
         sel='[data-ab-envpanel]:not([hidden]) .ks3-ab-bar[data-ab-rank="best"]',
         props={"background-color": "#12A150"}),
    dict(name="B11 advantage-bench · the worst bar is the data fill, not the alert",
         on=B11_ADV,
         sel='[data-ab-envpanel]:not([hidden]) .ks3-ab-bar[data-ab-rank="worst"]',
         props={"background-color": "#8FB7FF"}),
    dict(name="B11 advantage-bench · an unranked figure is muted mono",
         on=B11_ADV,
         sel="[data-ab-envpanel]:not([hidden]) .ks3-ab-chance:not([data-ab-rank])",
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "16px"}),
    dict(name="B11 advantage-bench · an unranked bar is the muted fill",
         on=B11_ADV,
         sel="[data-ab-envpanel]:not([hidden]) .ks3-ab-bar:not([data-ab-rank])",
         props={"background-color": "#C6B9A7"}),
    dict(name="B11 advantage-bench · the reason under the bar reads in on-dark body",
         on=B11_ADV, sel="[data-ab-envpanel]:not([hidden]) .ks3-ab-why",
         props={"color": "#E7DECE", "font-size": "17px"}),
    # ⚖️ THE VERDICT IS THE PAGE GROUND ON AN INK BLOCK — cream inside ink, and
    # the one place in this instrument where the text has to be INK and not
    # on-dark. It is the element the whole switch exists to reach, and it is
    # ONE TONE: the bench says what just happened, never whether anybody was
    # right (schema §0.7).
    dict(name="B11 advantage-bench · the verdict is the page ground on an ink block",
         on=B11_ADV, sel="[data-ab-envpanel]:not([hidden]) .ks3-ab-verdict",
         props={"background-color": "#FBF3E6", "color": "#221E1B",
                "font-size": "18px"}),
    # ── driven: three conditions switched through, ending on the tie ──
    dict(name="B11 advantage-bench · the tied column marks nothing best",
         on=B11_ADV, drive="b11-conditions-tried",
         sel="[data-ab-envpanel]:not([hidden]) .ks3-ab-bar",
         props={"background-color": "#C6B9A7"}),
    dict(name="B11 advantage-bench · the tied column's figures are all muted",
         on=B11_ADV, drive="b11-conditions-tried",
         sel="[data-ab-envpanel]:not([hidden]) .ks3-ab-chance",
         props={"color": "#C6B9A7"}),

    # ── b11-02 · selection-runner ──
    dict(name="B11 selection-runner · the bark label is muted mono",
         on=B11_SEL, sel=".ks3-nr-tabslabel",
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "14px", "text-transform": "uppercase"}),
    dict(name="B11 selection-runner · the chosen bark is the alert ground",
         on=B11_SEL, sel='.ks3-nr-tab[aria-pressed="true"]',
         props={"background-color": "#FFC53D", "color": "#221E1B",
                "min-height": "44px"}),
    dict(name="B11 selection-runner · an unchosen bark stays on the block ground",
         on=B11_SEL, sel='.ks3-nr-tab[aria-pressed="false"]',
         props={"background-color": "#3E3730", "color": "#FBF3E6"}),
    dict(name="B11 selection-runner · the bench sits on the nested dark panel",
         on=B11_SEL, sel=".ks3-nr-panel", props={"background-color": "#3E3730"}),
    dict(name="B11 selection-runner · what the bark IS reads muted, not body",
         on=B11_SEL, sel="[data-nr-barknote]:not([hidden])",
         props={"color": "#C6B9A7", "font-size": "18px"}),
    # ⚖️ THE CHART IS A FIXED-HEIGHT WELL AND THE COLUMNS SHARE IT. One column
    # fills it and twenty-four divide it, so the run reads as a run rather than
    # as a widening pile — which is why `flex: 1 1 0` and `min-width: 0` are
    # asserted rather than a width.
    dict(name="B11 selection-runner · the generations sit in a fixed well",
         on=B11_SEL, sel=".ks3-nr-chart",
         props={"height": "150px",
                "background-color": "rgba(255, 255, 255, 0.06)"}),
    dict(name="B11 selection-runner · a generation column shares the well",
         on=B11_SEL, sel="[data-nr-col]:not([hidden])",
         props={"min-width": "0px", "flex-grow": "1", "flex-shrink": "1"}),
    # ⚑ AMBER IS THE DARK MOTH HERE, NOT A MARK. There is no prediction on this
    # bench; the colour means "this many of them are the dark form", and the
    # word is on screen beside the number (R2). Recorded as a value so the day
    # the palette question is ruled the gate names it.
    dict(name="B11 selection-runner · the pale stack is the muted fill",
         on=B11_SEL, sel="[data-nr-col]:not([hidden]) .ks3-nr-pale",
         props={"background-color": "#C6B9A7"}),
    dict(name="B11 selection-runner · the dark stack is the alert fill",
         on=B11_SEL, sel="[data-nr-col]:not([hidden]) .ks3-nr-dark",
         props={"background-color": "#FFC53D"}),
    dict(name="B11 selection-runner · the axis caption is muted mono, uppercase",
         on=B11_SEL, sel=".ks3-nr-axis",
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "14px", "text-transform": "uppercase"}),
    dict(name="B11 selection-runner · the pale figure matches the pale stack",
         on=B11_SEL, sel='.ks3-nr-figure[data-nr-series="pale"]',
         props={"color": "#C6B9A7", "font-size": "19px",
                "font-weight": "700"}),
    dict(name="B11 selection-runner · the dark figure matches the dark stack",
         on=B11_SEL, sel='.ks3-nr-figure[data-nr-series="dark"]',
         props={"color": "#FFC53D", "font-size": "19px",
                "font-weight": "700"}),
    dict(name="B11 selection-runner · the note reads in on-dark body on a well",
         on=B11_SEL, sel=".ks3-nr-note:not([hidden])",
         props={"color": "#E7DECE", "font-size": "18px",
                "background-color": "rgba(255, 255, 255, 0.06)"}),
    dict(name="B11 selection-runner · the run buttons are inverted on ink",
         on=B11_SEL, sel=".ks3-nr-ten",
         props={"background-color": "#FBF3E6", "color": "#221E1B",
                "min-height": "44px"}),
    dict(name="B11 selection-runner · the reset is inverted on ink too",
         on=B11_SEL, sel=".ks3-nr-reset",
         props={"background-color": "#FBF3E6", "color": "#221E1B"}),
    # ── driven: ten generations on sooty bark ──
    dict(name="B11 selection-runner · a run fills the well with columns",
         on=B11_SEL, drive="b11-generations-run",
         sel="[data-nr-col]:not([hidden])",
         props={"min-width": "0px"}),

    # ── b11-03 · pressure-bench ──
    dict(name="B11 pressure-bench · an axis label is muted mono",
         on=B11_PRESS, sel=".ks3-pb-tabslabel",
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "14px", "text-transform": "uppercase"}),
    dict(name="B11 pressure-bench · the chosen species is the alert ground",
         on=B11_PRESS, sel='.ks3-pb-tab[data-pb-species][aria-pressed="true"]',
         props={"background-color": "#FFC53D", "color": "#221E1B",
                "min-height": "44px"}),
    dict(name="B11 pressure-bench · the chosen pressure is the alert ground too",
         on=B11_PRESS, sel='.ks3-pb-tab[data-pb-pressure][aria-pressed="true"]',
         props={"background-color": "#FFC53D", "color": "#221E1B"}),
    dict(name="B11 pressure-bench · an unchosen tab stays on the block ground",
         on=B11_PRESS, sel='.ks3-pb-tab[aria-pressed="false"]',
         props={"background-color": "#3E3730", "color": "#FBF3E6"}),
    dict(name="B11 pressure-bench · the bench sits on the nested dark panel",
         on=B11_PRESS, sel=".ks3-pb-panel", props={"background-color": "#3E3730"}),
    dict(name="B11 pressure-bench · the species name is on-dark at 21px",
         on=B11_PRESS, sel="[data-pb-speciespanel]:not([hidden]) .ks3-pb-name",
         props={"color": "#FBF3E6", "font-size": "21px",
                "font-weight": "700"}),
    dict(name="B11 pressure-bench · a trait reads in on-dark body",
         on=B11_PRESS, sel="[data-pb-speciespanel]:not([hidden]) .ks3-pb-trait",
         props={"color": "#E7DECE", "font-size": "17px"}),
    dict(name="B11 pressure-bench · a trait's name is muted mono at 13px",
         on=B11_PRESS,
         sel="[data-pb-speciespanel]:not([hidden]) .ks3-pb-traitlabel",
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "13px", "text-transform": "uppercase"}),
    # ⚖️ THE DIVIDER IS THE ARGUMENT'S HINGE — what the species IS, above; what
    # happens to it, below. A rule and not a gap, so the two read as one panel.
    dict(name="B11 pressure-bench · a rule divides the species from the pressure",
         on=B11_PRESS, sel=".ks3-pb-under",
         props={"border-top-width": "2px", "border-top-style": "solid"}),
    dict(name="B11 pressure-bench · the pressure headline is on-dark at 19px",
         on=B11_PRESS, sel="[data-pb-pressurepanel]:not([hidden]) .ks3-pb-pname",
         props={"color": "#FBF3E6", "font-size": "19px",
                "font-weight": "700"}),
    dict(name="B11 pressure-bench · what the pressure does reads muted",
         on=B11_PRESS, sel="[data-pb-pressurepanel]:not([hidden]) .ks3-pb-pnote",
         props={"color": "#C6B9A7", "font-size": "18px"}),
    dict(name="B11 pressure-bench · the outcome ask is on-dark at 17px",
         on=B11_PRESS, sel="[data-pb-cell]:not([hidden]) .ks3-pb-outlabel",
         props={"color": "#FBF3E6", "font-size": "17px",
                "font-weight": "600"}),
    dict(name="B11 pressure-bench · the outcome bar runs in a drawn track",
         on=B11_PRESS, sel="[data-pb-cell]:not([hidden]) .ks3-pb-track",
         props={"height": "18px",
                "background-color": "rgba(255, 255, 255, 0.08)"}),
    # ⚑ THREE BANDS, AND AMBER IS THE BOTTOM ONE AS DATA. Nothing is predicted
    # on this bench and nothing is marked; the band says "this population is in
    # trouble fifty years on" and the sentence underneath says which trouble.
    # The bench opens on the dormouse under habitat loss, which is 15% — the
    # worst cell on the bench — so the resting page measures the amber band.
    dict(name="B11 pressure-bench · a bottom-band outcome is amber and says so",
         on=B11_PRESS,
         sel='[data-pb-cell]:not([hidden]) .ks3-pb-outpct[data-pb-band="bad"]',
         props={"color": "#FFC53D", "font-family": "DM Mono",
                "font-size": "17px"}),
    dict(name="B11 pressure-bench · a bottom-band bar is the amber fill",
         on=B11_PRESS,
         sel='[data-pb-cell]:not([hidden]) .ks3-pb-bar[data-pb-band="bad"]',
         props={"background-color": "#FFC53D"}),
    # ⚠️ (0,2,0) — cream inside ink. Twenty individually-written sentences land
    # here and this is the only place the bench says anything at all.
    dict(name="B11 pressure-bench · the outcome text is the page ground on ink",
         on=B11_PRESS, sel="[data-pb-cell]:not([hidden]) .ks3-pb-why",
         props={"background-color": "#FBF3E6", "color": "#221E1B",
                "font-size": "18px"}),
    # ── driven: a top-band cell, and a middle-band cell ──
    dict(name="B11 pressure-bench · a top-band outcome is green",
         on=B11_PRESS, drive="b11-combinations-tried",
         sel='[data-pb-cell]:not([hidden]) .ks3-pb-outpct[data-pb-band="ok"]',
         props={"color": "#40DD84"}),
    dict(name="B11 pressure-bench · a top-band bar is the green fill",
         on=B11_PRESS, drive="b11-combinations-tried",
         sel='[data-pb-cell]:not([hidden]) .ks3-pb-bar[data-pb-band="ok"]',
         props={"background-color": "#12A150"}),

    # ── b11-04 · blight-bench ──
    dict(name="B11 blight-bench · the field label is muted mono",
         on=B11_BLIGHT, sel=".ks3-bb-tabslabel",
         props={"color": "#C6B9A7", "font-family": "DM Mono",
                "font-size": "14px", "text-transform": "uppercase"}),
    # ⊕ MRB-252 (RULED) — "which field am I looking at" is the plainest
    # selection use in the key stage, so it is the amber that moves. Ink on
    # `--ks3-data` is 8.18:1, better than ink on the alert had to be, and the
    # 44px target is asserted in the same row so a re-colour cannot quietly
    # take the tap size with it.
    dict(name="B11 blight-bench · the chosen field is the data ground, not the alert",
         on=B11_BLIGHT, sel='.ks3-bb-tab[aria-pressed="true"]',
         props={"background-color": "#8FB7FF", "color": "#221E1B",
                "min-height": "44px"}),
    dict(name="B11 blight-bench · an unchosen field stays on the block ground",
         on=B11_BLIGHT, sel='.ks3-bb-tab[aria-pressed="false"]',
         props={"background-color": "#3E3730", "color": "#FBF3E6"}),
    dict(name="B11 blight-bench · the bench sits on the nested dark panel",
         on=B11_BLIGHT, sel=".ks3-bb-panel", props={"background-color": "#3E3730"}),
    dict(name="B11 blight-bench · the field name is on-dark at 20px",
         on=B11_BLIGHT, sel="[data-bb-fieldpanel]:not([hidden]) .ks3-bb-name",
         props={"color": "#FBF3E6", "font-size": "20px",
                "font-weight": "700"}),
    dict(name="B11 blight-bench · what was planted reads muted, not body",
         on=B11_BLIGHT, sel="[data-bb-fieldpanel]:not([hidden]) .ks3-bb-note",
         props={"color": "#C6B9A7", "font-size": "18px"}),
    dict(name="B11 blight-bench · a bar's name is on-dark at 17px",
         on=B11_BLIGHT, sel="[data-bb-fieldpanel]:not([hidden]) .ks3-bb-barname",
         props={"color": "#FBF3E6", "font-size": "17px",
                "font-weight": "600"}),
    dict(name="B11 blight-bench · a bar runs in a drawn track",
         on=B11_BLIGHT, sel="[data-bb-fieldpanel]:not([hidden]) .ks3-bb-track",
         props={"height": "16px",
                "background-color": "rgba(255, 255, 255, 0.08)"}),
    # ⚖️ THE VARIATION BAR IS MUTED AND THE YIELD BAR IS AMBER, WHICH IS
    # DESIGN'S. The yield bar is the COST of variation — the reason a farmer
    # plants a clone — and it is drawn in the same ink as "nothing survived"
    # two rows above it. Flagged rather than repainted; ⚑ the third job amber
    # does on this page.
    dict(name="B11 blight-bench · the variation bar is the muted fill",
         on=B11_BLIGHT,
         sel='[data-bb-fieldpanel]:not([hidden]) .ks3-bb-bar[data-bb-tone="muted"]',
         props={"background-color": "#C6B9A7"}),
    dict(name="B11 blight-bench · the yield bar is amber, as the cost",
         on=B11_BLIGHT,
         sel='[data-bb-fieldpanel]:not([hidden]) .ks3-bb-bar[data-bb-tone="cost"]',
         props={"background-color": "#FFC53D"}),
    # ⚖️ THE RESTING FIELD IS PLANTED AND UNTOUCHED — every plant standing, a
    # full green bar at "1000 of 1000". That is what makes the release mean
    # something: a full field becomes an empty one, rather than an empty one
    # appearing.
    dict(name="B11 blight-bench · the unblighted field is a full green bar",
         on=B11_BLIGHT,
         sel='[data-bb-fieldpanel]:not([hidden]) [data-bb-surv="before"] .ks3-bb-bar',
         props={"background-color": "#12A150"}),
    # ⊕ NEW under MRB-252 · audit 3.4 — the survivor VALUE beside that bar was
    # one of the four measured violations (16px/400 at 3.48:1) and had no row
    # of its own; only the bar did. A fill and the text on top of it are two
    # different contrast questions and now they are two different rows.
    dict(name="B11 blight-bench · the survivor figure is the on-dark green, not the fill",
         on=B11_BLIGHT,
         sel='[data-bb-fieldpanel]:not([hidden]) [data-bb-surv="before"] .ks3-bb-value[data-bb-band="ok"]',
         props={"color": "#40DD84", "font-family": "DM Mono",
                "font-size": "16px"}),
    dict(name="B11 blight-bench · the release button is inverted on ink",
         on=B11_BLIGHT, sel=".ks3-bb-run",
         props={"background-color": "#FBF3E6", "color": "#221E1B",
                "min-height": "44px"}),
    dict(name="B11 blight-bench · the clear button is inverted on ink",
         on=B11_BLIGHT, sel=".ks3-bb-clear",
         props={"background-color": "#FBF3E6", "color": "#221E1B"}),
    # ── driven: the blight released on the clone field ──
    # ⚑⚑ ZERO IS ITS OWN BAND AND IT IS AMBER. The clone field does not do
    # badly, it returns NOTHING — `resistant: 0` over `varieties: 1` is zero
    # along every arithmetic path — and that number is the payoff of the whole
    # lesson. Amber is DATA here; the row prints "0 of 1000" beside the bar.
    dict(name="B11 blight-bench · a zero harvest is amber and says so",
         on=B11_BLIGHT, drive="b11-blight-released",
         sel='[data-bb-fieldpanel]:not([hidden]) [data-bb-surv="after"] .ks3-bb-value[data-bb-band="none"]',
         props={"color": "#FFC53D", "font-family": "DM Mono",
                "font-size": "16px"}),
    dict(name="B11 blight-bench · the zero-survivor bar is the amber fill",
         on=B11_BLIGHT, drive="b11-blight-released",
         sel='[data-bb-fieldpanel]:not([hidden]) [data-bb-surv="after"] .ks3-bb-bar[data-bb-band="none"]',
         props={"background-color": "#FFC53D"}),
    dict(name="B11 blight-bench · the verdict is the page ground on an ink block",
         on=B11_BLIGHT, drive="b11-blight-released",
         sel="[data-bb-fieldpanel]:not([hidden]) [data-bb-verdict]:not([hidden])",
         props={"background-color": "#FBF3E6", "color": "#221E1B",
                "font-size": "18px"}),
    dict(name="B11 blight-bench · the spent release button dims",
         on=B11_BLIGHT, drive="b11-blight-released",
         sel=".ks3-bb-run[disabled]", props={"opacity": "0.45"}),

    # ── b11-02 · the peppered moth pair (a `figure`, not a `practical`) ──
    # ⚑⚑ THESE FOUR ROWS EXIST TO CATCH ONE FAILURE, and it is the failure that
    # cost four rebuilds on the first drawer: `fill="var(--ks3-ink)"` as an SVG
    # PRESENTATION ATTRIBUTE is not a valid <paint>, the attribute is silently
    # dropped, and the element renders opaque BLACK — while every token grep in
    # the repo stays clean, because the tokens are all there, in the one place
    # where they do nothing. Only a computed read in a browser sees it, and
    # only if something asks for the resolved `fill`. These ask.
    dict(name="B11 moth pair · the pale moth is the band fill, not a dropped paint",
         on=B11_SEL,
         sel='.ks3-moth[data-moth-tone="pale"] path', props={"fill": "#F4E9D8"}),
    dict(name="B11 moth pair · the dark moth is the ink fill, not a dropped paint",
         on=B11_SEL, drive="b11-moth-pair",
         sel='.ks3-moth[data-moth-tone="dark"] path', props={"fill": "#221E1B"}),
    # ⚖️ THE TWO BARKS DIFFER BY TONE — and, structurally, by PATTERN, which
    # the drive checks by counting mottle against streaks. Tone alone would
    # make the diagram work for most readers and fail exactly the ones it is
    # drawn for.
    dict(name="B11 moth pair · the lichen bark is the band ground",
         on=B11_SEL,
         sel='.ks3-moth-bark[data-bark="lichen"]', props={"fill": "#F4E9D8"}),
    dict(name="B11 moth pair · the soot bark is the ink ground",
         on=B11_SEL,
         sel='.ks3-moth-bark[data-bark="soot"]', props={"fill": "#221E1B"}),
    # ═══ END B11 ═══ rows
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
    # ⊕ MRB-221 — the draft-marker contrast pair is deleted with the marker.
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
    # ⊕ MRB-257 · audit 3.19 — THE BAR MOVES FROM 3.0 TO 4.49, AND 4.49 IS NOT
    # A ROUNDED 4.5. It is the CEILING of this pairing, measured: `--ks3-ink`
    # #221E1B on `--ks3-accent` #E4572E is 4.490975:1, and #221E1B is the
    # darkest ink the key stage has. No implementation choice reaches AA here.
    #
    # Why not leave it at R1's 3.0 mark bar: this badge draws the letter
    # A/B/C/D at 15px/800, which is a letter a student reads, and bold under
    # 18.66px is not large text. At 3.0 the row passed at 3.34:1 — cream on the
    # accent — while `--ks3-accent`'s own annotation read "LARGE TEXT ONLY.
    # Never body size". The gate was licensing exactly what the token forbade.
    #
    # Why not 4.5: the ruled fix would then fail by nine thousandths and the
    # only ways to pass would be to change `--ks3-accent` itself or to stop
    # filling the badge with it — both brand decisions, both Mide's, neither
    # this pass's to take. Pinning the ceiling is the strongest honest
    # assertion available: cream (3.34) fails it, and any future drift in the
    # accent that lowers the pairing fails it too. ⚑ FOR MIDE: the accent fill
    # cannot carry body-size text at AA. Reported, not hidden.
    dict(name="MARK activity CHOSEN badge letter on accent", on=LESSON,
         drive="activity-chosen",
         fg='.ks3-check .ks3-option[aria-pressed="true"] .ks3-opt-mark',
         bg='.ks3-check .ks3-option[aria-pressed="true"] .ks3-opt-mark',
         need=4.49),
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
    # ⊕ MRB-257 · audit 3.21 — THE EXEMPTION GOES, because the thing it
    # excused is fixed. This row measured 2.63:1 and passed by claiming WCAG
    # 1.4.3's inactive-component carve-out, which was true and was also the
    # reason nobody looked again. `--ks3-ink-faint` on the band is 4.75:1, so
    # the pair now clears the bar a letter needs on merit — and the escape
    # hatch is removed rather than left standing, so it cannot quietly cover a
    # regression back to 2.63.
    dict(name="MARK ladder SPENT badge glyph on band", on=LESSON,
         drive="ladder-answered",
         fg='.ks3-rung[data-mode="marked"] .ks3-option.is-spent .ks3-opt-mark',
         bg='.ks3-rung[data-mode="marked"] .ks3-option.is-spent .ks3-opt-mark',
         need=4.5),
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
    # ⊕ MRB-221 — the draft-badge contrast pair is deleted with the badge.
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

    # ═══ MRB-257 · the WS3 contrast batch ═══════════════════════════════
    #
    # Every pair below is a surface the audit measured failing and no row in
    # this list was watching. That is the finding under the finding: the gate
    # had 56 pairs, all on the page shell and the shared block vocabulary, and
    # none on an instrument's readouts — which is exactly where a student reads
    # a number and where six of these live.
    #
    # `need` is R1's: 4.5 for text, 3.0 for a state-bearing mark. Where a value
    # is drawn at 26px/800 and therefore qualifies as large text, it is STILL
    # registered at 4.5 here, because these all clear it comfortably and a bar
    # set at the legal minimum lets a regression halfway back pass in silence.

    # ── the three tokens MRB-252 ruled, each on a page that renders it ──
    #
    # ⚖️ `--ks3-ok-dark` IS PINNED ON THE TILE, NOT THE PANEL. b9-06's figures
    # sit on `.ks3-qb-figures`, an rgba(255,255,255,.06) well that composites
    # to #4A433C — one step lighter than `--ks3-dark-panel`, and the step that
    # took the old green under even the LARGE-text bar at 2.89:1. A token
    # measured only against the darker ground would have passed a value that
    # fails here, so the binding ground is the one that binds.
    dict(name="TOKEN --ks3-ok-dark · revealed total on the b9-06 figures tile",
         on=B9_QUADRAT, drive="b9-field-revealed",
         fg='[data-qb-figure="real"][data-revealed] .ks3-qb-figvalue',
         bg=".ks3-qb-figures", need=4.5),
    dict(name="TOKEN --ks3-ok-dark · predator readout on the dark panel",
         on=B9_CYCLE, fg='.ks3-cy-live[data-series="pred"]',
         bg=".ks3-cy-panel", need=4.5),
    dict(name="TOKEN --ks3-ok-dark · top-band outcome on the b11-03 panel",
         on=B11_PRESS, drive="b11-combinations-tried",
         fg='[data-pb-cell]:not([hidden]) .ks3-pb-outpct[data-pb-band="ok"]',
         bg="[data-pb-cell]:not([hidden])", need=4.5),
    # ⚖️ `--ks3-data` CARRIES A DUAL CONSTRAINT and both ends are measured: it
    # is text on ink on b11-01, and a FILL that ink sits on on b11-04. A colour
    # that only ever passed one of those would be half a token.
    dict(name="TOKEN --ks3-data · the worst-in-column figure, as text on ink",
         on=B11_ADV,
         fg='[data-ab-envpanel]:not([hidden]) .ks3-ab-chance[data-ab-rank="worst"]',
         bg="[data-ab-envpanel]:not([hidden])", need=4.5),
    dict(name="TOKEN --ks3-data · ink ON it, on the chosen field tab",
         on=B11_BLIGHT, fg='.ks3-bb-tab[aria-pressed="true"]',
         bg='.ks3-bb-tab[aria-pressed="true"]', need=4.5),
    # ⚖️ `--ks3-ok-text` did not change value and is registered anyway. MRB-252
    # widened its annotation from "5.9:1 on tint" to a claim about EVERY light
    # ground it lands on, and an annotation that is law needs a measurement
    # behind it. The ladder's correct-answer verdict is the ground it lands on
    # most often and the one a student reads at the moment it matters.
    dict(name="TOKEN --ks3-ok-text · the correct verdict on its own tint",
         on=LESSON, drive="ladder-answered",
         fg=".ks3-feedback.is-correct", bg=".ks3-feedback.is-correct", need=4.5),

    # ── audit 3.2 · the comparison captions, on the phone layout ──
    # Below 880px the header row is `display: none` and these four strings are
    # the only thing saying which column is which. They measured 1.78:1.
    dict(name="comparison column caption on the dark table (audit 3.2)",
         on=B5_CMP, fg=".ks3-dark .ks3-cmp-cap", bg=".ks3-dark .ks3-cmp-table",
         need=4.5),

    # ── audit 3.6 · the section rail, which had no row at all ──
    # A live `<a>`, and on desktop the only in-page navigation there is. Both
    # halves: the 11px mono label and the 16px/800 chip, which is bold under
    # 18.66px and so needs 4.5 and not 3.0.
    #
    # ⚠️ `:not(.is-current):not(.is-done)` IS LOAD-BEARING AND WAS FOUND BY
    # MUTATION. Written as a bare `.ks3-rail-label` these two rows measured
    # 15.02:1 and 16.14:1 and could not be made to fail: `wireRail` marks the
    # FIRST stop `is-current` on load, `querySelector` returns the first match,
    # and `is-current` has always been ink. So the rows were measuring the one
    # state of the rail that already passed, and reverting the fix left them
    # green — an assertion incapable of failing, which is the exact defect
    # `ks3_mutation.py` exists to expose. The audit's finding is about the
    # stops a student has NOT reached, and now so is the row.
    dict(name="rail label, stage not yet reached (audit 3.6)", on=LESSON,
         fg=".ks3-rail li:not(.is-current):not(.is-done) .ks3-rail-label",
         bg="body", need=4.5),
    dict(name="rail chip number, stage not yet reached (audit 3.6)", on=LESSON,
         fg=".ks3-rail li:not(.is-current):not(.is-done) .ks3-rail-chip",
         bg=".ks3-rail li:not(.is-current):not(.is-done) .ks3-rail-chip",
         need=4.5),

    # ── audit 3.18 · the commit instruction on a cream gate ──
    # Formally this is large text (22px/700) and the requirement is 3:1; it is
    # registered at 4.5 because the fix lands 6.43:1 and because it is a
    # SENTENCE the block asks the student to act on, not a number. A bar at 3.0
    # would let it drift back to 3.5:1 without a word.
    dict(name="switch-bench commit instruction on cream (audit 3.18)",
         on=B2_SKEL, fg=".ks3-switch-predict .ks3-commit",
         bg=".ks3-switch-panel", need=4.5),

    # ── audit 3.13 · the rule card's badge, the accent's other body-size use ──
    # ⚑ 4.49, not 4.5, and for the reason set out beside the option badge
    # above: `--ks3-ink` on `--ks3-accent` measures 4.490975:1 and that is the
    # ceiling of the pairing, not a rounding of AA. Cream, which is what this
    # shipped as, is 3.34 and fails the row.
    dict(name="rule-card badge initials on the accent fill (audit 3.13)",
         on=B10_MODEL, fg=".ks3-rule-badge", bg=".ks3-rule-badge", need=4.49),

    # ── audit 3.5 / 3.7 / 3.8 · the dimmed states, as RATIOS ──
    #
    # These are the rows the old contrast layer could not have carried at all.
    # It read `color` and a stack of background colours and knew nothing about
    # `opacity`, so a row dimmed to 45% reported the undimmed 6.08:1 and passed
    # while a browser painted 2.48:1. Now that `_flatten` and `measure_d`
    # composite the opacity chain, the dim states can be asserted as what they
    # actually are — a contrast number — and not only as the opacity value that
    # produces it. Both are kept: the `props` opacity rows say WHAT the dim is,
    # these say what it COSTS, and a change to the ground under a row would
    # move one and not the other.
    #
    # The text is the science itself: "Algae", "Water fleas", "A chromosome",
    # "10% of the original", and it is on screen from the first paint because
    # the whole chain is drawn from the start so a student can see how far
    # there is to go.
    dict(name="an unreached chain level's role, dimmed (audit 3.5)",
         on=B9_CHAIN,
         fg=".ks3-cl-levels:not([hidden]) .ks3-cl-level:not([data-shown]) .ks3-cl-levelrole",
         bg=".ks3-cl-panel", need=4.5),
    dict(name="an unreached food-chain link's number, dimmed (audit 3.7)",
         on=B7_TRACE,
         fg=".ks3-tb-food:not([hidden]) .ks3-tb-link:not([data-shown]) .ks3-tb-num",
         bg=".ks3-tb-panel", need=4.5),
    # The A/B/C/D letter on a fault the student did NOT pick, after "Check it"
    # — the state in which they read what was wrong. 2.70:1 as it shipped, and
    # it needed both halves of the fix: the dim raised AND the letter moved off
    # `--ks3-on-dark-muted`, because .65 alone would only have reached ~3.5.
    dict(name="a spent fault's letter, dimmed (audit 3.8)",
         on=B6_CLAIMS, drive="claims-checked",
         fg='.ks3-ccheck-fault[disabled][aria-pressed="false"] .ks3-ccheck-mark',
         bg=".ks3-ccheck-panel", need=4.5),
    # ⊖ NO ROW FOR audit 3.21's LOCKED BUTTONS, deliberately. WCAG 1.4.3
    # exempts an inactive component and the audit says so twice; asserting 4.5
    # on a disabled control would be this gate inventing a requirement, and the
    # next person to meet it would have to argue with it rather than with the
    # standard. What holds 3.21 is the `opacity: 0.65` props rows, which pin
    # the decision that was actually taken. Measured after the fix for the
    # record: the locked reveal button paints #FCF6EB on #6F6C67 = 4.86:1,
    # from 2.71:1.
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


# ⊖ TWO KNOWN OFFENDERS, NAMED RATHER THAN EXCUSED (MRB-248, 18 Aug 2026).
#
# `check_rail_reachable`'s own docstring already names these two: c1-05's
# `#s-scale` is three static cards and two paragraphs, and c1-02's `#s-matrix`
# is a static contrast grid. Both are rail stops, both carry `data-instrument`
# because the block owns its own options, and NEITHER wire function calls
# `markStage` — so neither can declare a completion at 0 without shipping a
# stop that can then never tick. Fixing them properly means giving each a
# completion predicate, which is a change to ticking behaviour on two lessons
# that are live and in front of students, and it is not this run's to make.
#
# ⚠️ THE LIST SELF-CLEARS. An entry naming a section that no longer offends is
# a build failure, so a fix cannot leave a stale exemption behind and the list
# cannot quietly grow into a way of not fixing things.
# ⚖️ RULED 18 Aug 2026 — THESE TWO STAY PARKED FOR NOW, and the ruling is
# recorded here rather than in a ticket because this set is where the next pass
# will meet the question.
#
# Both are rail stops on LIVE C1 lessons whose wire functions never call
# `markStage`, so they can never tick and the student can never reach 4 of 4 on
# those two pages. That is worse than the `done_when` case contract R2 parked,
# because R2's defect was invisible to a student and this one is a counter that
# stops short in front of them.
#
# It is still not this run's work, for two reasons that are about risk rather
# than tidiness:
#
#   1. The fix is not a line — it is DECIDING WHAT COMPLETION MEANS for two
#      instruments nobody in this run has read. `#s-scale` and `#s-matrix` are
#      c1-05's and c1-02's, and inventing a predicate for an instrument you have
#      not studied is how a stop starts ticking when it should not, which is the
#      B1 finding quoted inside `doneByDom()`.
#   2. Changing ticking behaviour on two lessons that are live, verified and in
#      front of students, at the end of a nine-lesson biology run, is the shape
#      of change that gets made at the end of a long session and found in the
#      morning.
#
# What makes parking safe here is that this set SELF-CLEARS: a stale entry fails
# the build, so the exemption cannot outlive the defect quietly. It is a
# reminder with teeth, which is the only kind worth leaving.
#
# ⚠️ Whoever takes it: the answer is probably `mirrors`, not a new predicate.
# `ks3_rail_manifest.py` already derives these two as mirrors from Design's own
# `isDone()` — its docstring names them — so the completion they need may
# already exist on the instrument beside them.
_TICK_EXEMPT = {
    ("chemistry/particles-and-their-behaviour/diffusion.html", "s-scale"),
    ("chemistry/particles-and-their-behaviour/solids-liquids-and-gases.html",
     "s-matrix"),
}


def check_nothing_ticks_on_load(ks3_root):
    """⊕ MRB-248 / B11 — MRB-208's other half, and it had no gate either.

    "Nothing is ticked on load" has been settled since MRB-208 and the way it
    is kept is that every instrument emits `data-stage-done="0"` in its own
    dispatch entry. Nothing checked that it did. `check_rail_reachable` above
    asks whether a section carries ANY completion signal, and an instrument
    that dropped the declaration still carries `class="ks3-option"` — so it
    passes that gate and then `doneByDom()` falls through to "anything in here
    is aria-pressed", which on nearly every bench in the key stage is TRUE
    BEFORE THE STUDENT HAS DECIDED ANYTHING, because a tab is pressed to show
    where the bench is standing.

    ⚠️ AND A BROWSER CANNOT SEE IT. `markStage` writes the attribute on the
    first `draw()`, so by the time any drive reads the DOM the value is there
    and correct. What is wrong is the SHIPPED BYTES: the rail's own first paint
    runs before the instruments wire, and a crawler or a reader with JS off
    gets a page whose rail claims work nobody did. So this is read out of the
    HTML as written, which is the only place the defect exists.

    Found by mutation: removing the declaration from one dispatch entry left
    every other gate in the build green.
    """
    problems, total = [], 0
    seen_exempt, stale = set(), set()
    for page in _lesson_pages(ks3_root):
        rel = os.path.relpath(page, ks3_root)
        html = open(page, encoding="utf-8").read()
        # ⚠️ SCOPED TO INSTRUMENTS THAT ARE RAIL STOPS, and the scope is the
        # correctness of the check rather than a softening of it. A
        # `confrontation` carries `data-instrument` — it owns its own options —
        # and carries no completion contract on purpose: it is static, it asks
        # for nothing, and MRB-249 records that `#s-think` is on no rail on any
        # page. Requiring a declaration there would fail fifty-six live pages
        # over a rule that does not apply to them. What the rule is about is a
        # stop that can tick, so the anchors the rail names are the scope.
        anchors = set(re.findall(r"&quot;anchor&quot;:&quot;([a-z0-9-]+)&quot;",
                                 html))
        for m in re.finditer(r"<section[^>]*\bdata-instrument\b[^>]*>", html):
            tag = m.group(0)
            sid = re.search(r'\bid="([^"]+)"', tag)
            if not sid or sid.group(1) not in anchors:
                continue
            total += 1
            key = (rel.replace(os.sep, "/"), sid.group(1))
            if 'data-stage-done="0"' in tag:
                if key in _TICK_EXEMPT:
                    stale.add(key)
                continue
            if key in _TICK_EXEMPT:
                seen_exempt.add(key)
                continue
            problems.append(
                "MRB-208: /%s ships an instrument section with %s — every "
                "instrument declares its own completion at 0 in the bytes, or "
                "`doneByDom()` falls through to \"anything in here is "
                "aria-pressed\", which is true before the student has decided "
                "anything. A browser cannot catch this: `markStage` writes the "
                "attribute on the first draw."
                % (rel, "data-stage-done=\"1\"" if 'data-stage-done="1"' in tag
                   else "no `data-stage-done` at all"))
    for key in sorted(_TICK_EXEMPT - seen_exempt):
        problems.append(
            "MRB-208: /%s #%s is on the known-offender list and no longer "
            "offends (or no longer exists). The list self-clears: remove the "
            "entry, so it can never become a way of not fixing something."
            % key)
    for key in sorted(stale):
        problems.append(
            "MRB-208: /%s #%s declares completion at 0 and is still exempt. "
            "Remove the exemption." % key)
    return problems, total


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
        by_anchor = {st.get("anchor"): st for st in stages if st.get("anchor")}
        for st in stages:
            anchor = st.get("anchor")
            if not anchor:
                continue                  # ditto
            label = st.get("short") or anchor
            total += 1

            # ⊕ MRB-249 — a stop may MIRROR an earlier stop instead of carrying
            # its own signal. Design's `isDone()` returns the same expression
            # for two consecutive ids on 33 of her 48 pages: the synthesis
            # section is the payoff of the instrument beside it and takes no
            # commitment of its own, because the instrument already did.
            #
            # A mirror is only a completion route if it TERMINATES somewhere
            # that can actually finish, so the chain is walked to a real
            # section and that section is what gets checked. A mirror naming a
            # stop that is not on this rail, or a cycle, is a stop that can
            # never tick — the same failure, reached by a new route, and it is
            # reported as such rather than silently accepted.
            hops, at, seen = 0, st, {anchor}
            while (at.get("mirrors") or "").strip():
                target = at["mirrors"]
                if target not in by_anchor:
                    problems.append(
                        "%s: rail stop %r mirrors %r, which is not a stop on "
                        "this rail — it can never tick"
                        % (name, label, target))
                    at = None
                    break
                if target in seen:
                    problems.append(
                        "%s: rail stop %r is in a mirror cycle through %r, so "
                        "it can never tick" % (name, label, target))
                    at = None
                    break
                seen.add(target)
                at = by_anchor[target]
                hops += 1
            if at is None:
                continue
            if hops:
                # The mirrored stop's own reachability is checked on its own
                # iteration; this stop rides on it and needs nothing further.
                if not (st.get("done_when") or "").strip():
                    problems.append(
                        "%s: rail stop %r declares no done_when — every stop "
                        "has to name the condition that completes it"
                        % (name, label))
                continue

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




def check_rail_matches_design(ks3_root, repo_root):
    """⊕ MRB-249 — the built rail is the rail DESIGN DREW, stop for stop.

    `check_rail_reachable` asks whether the stops we emitted can tick. It
    cannot ask about a stop we never emitted, and that is precisely how the
    defect escaped it: across B3, B4, B5, B6, B7 and B8, **33 pages shipped a
    three-stop rail where Design drew four**, each dropping the synthesis
    section between the instrument and the ladder.

    Every one of those sections is still in the built page, still carrying its
    anchor, holding 1.2–5.2 KB of teaching — a drawn equation, a summary table,
    a set of fact cards. Three separate authoring passes reasoned that a
    section with no control of its own "cannot tick" and took it off the rail,
    which made the reachability gate pass. The gate was narrower than its own
    name, and it read as coverage.

    That reasoning contradicts MRB-205 — Design draws, we render, and the page
    wins over the engine — and it contradicts Design's own `isDone()`, which
    states in plain JavaScript how the stop ticks:

        if (id === 's-bench')   return s.exits;
        if (id === 's-summary') return s.exits;

    So this asserts against an outside reference the build cannot talk itself
    out of: `docs/ks3/rail-manifest.md`, generated from Design's delivered
    pages by `ks3_rail_manifest.py`.

    Three assertions, and the third is the one that closes the hole:

    1. Anchors match the drawn rail exactly, and IN ORDER. A dropped stop, an
       added stop and a reordered rail all fail.
    2. The mirror map matches, so a stop cannot be kept on the rail by being
       quietly re-pointed at some other section's state.
    3. A rail-bearing page with NO row in the manifest fails. Without this the
       gate is opt-in, and a unit could pass by never being recorded at all —
       the same defect class, one level up.
    """
    problems, total = [], 0
    rails = RAIL_MANIFEST.manifest_rails(repo_root)
    for page in _lesson_pages(ks3_root):
        with open(page, encoding="utf-8") as fh:
            html = fh.read()
        name = os.path.basename(page)
        slug = name[:-len(".html")]
        found = re.search(r'data-rail-stages="([^"]*)"', html)
        if not found:
            continue
        try:
            stages = json.loads(_unescape(found.group(1)))
        except ValueError:
            continue                      # check_rail_anchors owns this failure
        total += 1

        drawn = rails.get(slug)
        if drawn is None:
            problems.append(
                "%s: carries a rail but has no row in %s. Regenerate it with "
                "`python3 ks3_rail_manifest.py --write` so the drawn rail is on "
                "the record — an unrecorded lesson is unchecked, not passing."
                % (name, RAIL_MANIFEST.MANIFEST))
            continue
        want_ids, want_mirrors = drawn
        if want_ids is None:
            continue                      # Design drew no RAIL const for this one

        got_ids = [st.get("anchor") for st in stages]
        if got_ids != want_ids:
            missing = [i for i in want_ids if i not in got_ids]
            added = [i for i in got_ids if i not in want_ids]
            detail = ""
            if missing:
                detail += "  DROPPED: %s" % ", ".join(missing)
            if added:
                detail += "  ADDED: %s" % ", ".join(added)
            problems.append("%s: rail is %s, Design draws %s.%s"
                            % (name, got_ids, want_ids, detail))
            continue

        got_mirrors = dict((st["anchor"], st["mirrors"]) for st in stages
                           if (st.get("mirrors") or "").strip())
        if got_mirrors != want_mirrors:
            problems.append(
                "%s: mirror map is %s, Design's isDone() gives %s"
                % (name, got_mirrors or {}, want_mirrors or {}))
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
  //
  // ⊕ MRB-257 — AND THE `opacity` OF EVERY LEVEL WITH IT. This used to return
  // background colours alone, which makes the gate blind to the single most
  // common way KS3 loses contrast: an ancestor at `opacity: .45`. CSS renders
  // such an element's whole subtree into a group and composites the GROUP, so
  // a row dimmed to .45 paints `--ks3-on-dark-muted` as #7B7266 and not
  // #C6B9A7 — 2.48:1 rather than 6.08:1, on text a student is meant to read.
  // Audit findings 3.5, 3.7, 3.8 and 3.21 are all that one mechanism, 40-odd
  // elements of it, and not one of them could have been caught here.
  groundStack: function (sel) {
    var el = document.querySelector(sel);
    if (!el) { return null; }
    var out = [];
    while (el) {
      var cs = getComputedStyle(el);
      out.push({bg: cs.backgroundColor, op: cs.opacity});
      el = el.parentElement;
    }
    out.push({bg: getComputedStyle(document.body).backgroundColor, op: "1"});
    return out;
  },
  // The product of `opacity` from an element out to the root. What a text
  // colour's own alpha has to be multiplied by before it is composited.
  opacityChain: function (sel) {
    var el = document.querySelector(sel);
    if (!el) { return null; }
    var k = 1;
    while (el) {
      var v = parseFloat(getComputedStyle(el).opacity);
      if (!isNaN(v)) { k *= v; }
      el = el.parentElement;
    }
    return k;
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
    # ═══ BEGIN B4 ═══ drives
    #
    # ⚠️ EVERY B4 DRIVE IS STRUCTURAL, NOT KEYED ON AN AUTHORED ID. B3's
    # `gut-stomach` reaches its panel by `data-stop="stomach"`, which is right
    # when the engine and the content ship in one pass. B4's five instruments
    # were engineered before their lessons were authored, so a drive that named
    # `co2` or `dawn` would be asserting a payload nobody had written yet — and
    # would fail as a colour regression on the day an author chose a different
    # id. These reach the state they want through the instrument's own
    # controls, by position or by computing it from the instrument's own
    # attributes, and every one asserts the invariant it drove for.

    # Commits a prediction on every gas row and opens the two bags. Reached
    # through the choice buttons and the reveal button, never by setting an
    # attribute — which is also what makes it a test of the lock.
    "gas-revealed": r"""
(function () {
  var sec = document.querySelector('[data-gasblock]');
  if (!sec) { return "no gas-compare on the page"; }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on load";
  }
  var w = sec.querySelector('[data-gas]');
  var rows = w ? w.querySelectorAll('.ks3-gas-row') : [];
  if (rows.length < 2) { return "the block draws fewer than two gas rows"; }
  var btn = w.querySelector('[data-gas-open]');
  if (!btn) { return "the block has no reveal button"; }
  if (!btn.disabled) {
    return "the reveal was open before a single prediction was committed";
  }
  for (var i = 0; i < rows.length; i++) {
    var choices = rows[i].querySelectorAll('.ks3-gas-choice');
    if (choices.length < 2) { return "a gas row offers fewer than two choices"; }
    // The FIRST choice on every row, so some rows are right and some wrong —
    // which is the state the verdict styling has to survive.
    choices[0].click();
    if (i < rows.length - 1 && !btn.disabled) {
      return "the reveal unlocked before every row was committed";
    }
  }
  if (btn.disabled) { return "the reveal is still locked with every row committed"; }
  btn.click();
  var table = w.querySelector('[data-gas-table]');
  var close = w.querySelector('[data-gas-close]');
  if (!table || table.hasAttribute('hidden')) {
    return "the two bags were analysed and the table is still hidden";
  }
  if (!close || close.hasAttribute('hidden')) {
    return "the table arrived without its closing paragraph";
  }
  // ⚠️ THE CLAMP. Every bar must be drawn wide enough to see, including the
  // 0.04% one, and every cell must carry its numeral beside it — the numeral
  // is the correction to the clamp and the block is dishonest without it.
  var bars = w.querySelectorAll('.ks3-gas-bar');
  for (var b = 0; b < bars.length; b++) {
    if (bars[b].getBoundingClientRect().width < 1) {
      return "a gas bar was drawn at zero width; the clamp is not applied";
    }
  }
  var nums = w.querySelectorAll('.ks3-gas-cell .ks3-gas-num');
  if (nums.length !== bars.length) {
    return "a bar is drawn without the numeral that corrects it";
  }
  var marked = w.querySelectorAll('.ks3-gas-row[data-verdict]');
  if (marked.length !== rows.length) {
    return "the reveal did not record a verdict on every row";
  }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "the two bags were analysed and the stop did not tick";
  }
  return "";
})()
""",

    # Drives the diaphragm to the fullest inhale the instrument offers, by
    # taking the HIGHEST preset rather than a named one.
    "bell-in": r"""
(function () {
  var sec = document.querySelector('[data-bellblock]');
  if (!sec) { return "no bell-jar on the page"; }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on load";
  }
  var w = sec.querySelector('[data-bell]');
  var slider = w ? w.querySelector('[data-bell-slider]') : null;
  if (!slider) { return "the bell jar has no diaphragm slider"; }
  var rest = Number(w.getAttribute('data-rest'));
  var presets = w.querySelectorAll('[data-preset]');
  if (presets.length < 2) { return "the bell jar draws fewer than two presets"; }
  var top = null, best = -1;
  for (var i = 0; i < presets.length; i++) {
    var v = Number(presets[i].getAttribute('data-preset'));
    if (v > best) { best = v; top = presets[i]; }
  }
  if (best <= rest) { return "no preset drives the diaphragm past its resting position"; }
  var restChain = w.querySelector('[data-chain="rest"]');
  if (!restChain || restChain.hasAttribute('hidden')) {
    return "the block did not open on its resting chain";
  }
  top.click();
  var chain = w.querySelector('[data-chain="in"]');
  if (!chain || chain.hasAttribute('hidden')) {
    return "the diaphragm was contracted and the inhale chain is still hidden";
  }
  if (w.querySelectorAll('.ks3-bell-chain:not([hidden])').length !== 1) {
    return "more than one chain is showing at once";
  }
  // ⚠️ FOUR STEPS, MUSCLE FIRST AND AIR LAST. This is the instrument. If the
  // count ever drops or the order is rebuilt from something other than the
  // authored list, it shows up here rather than in a reader's confusion.
  var steps = chain.querySelectorAll('.ks3-bell-step');
  if (steps.length !== 4) {
    return "the causal chain is drawing " + steps.length + " steps, not four";
  }
  for (var s = 0; s < steps.length; s++) {
    if (!steps[s].textContent.replace(/\s/g, '')) {
      return "chain step " + (s + 1) + " arrived empty";
    }
    if (steps[s].textContent.indexOf('{') >= 0) {
      return "a chain step shipped with an unfilled placeholder: "
        + steps[s].textContent;
    }
  }
  var reads = w.querySelectorAll('.ks3-bell-read dd');
  for (var r = 0; r < reads.length; r++) {
    if (reads[r].textContent.indexOf('{') >= 0) {
      return "a readout shipped with an unfilled placeholder: " + reads[r].textContent;
    }
  }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "the model was worked and the stop did not tick";
  }
  return "";
})()
""",

    # Stops BOTH flows — the state a student is most likely to misread as
    # nothing happening, and the one where the outward bar has to stay drawn.
    "cross-both-stopped": r"""
(function () {
  var sec = document.querySelector('[data-crossblock]');
  if (!sec) { return "no crossing-counter on the page"; }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on load";
  }
  var w = sec.querySelector('[data-cross]');
  var sw = w ? w.querySelectorAll('[data-switch]') : [];
  if (sw.length !== 2) { return "the counter draws " + sw.length + " switches, not two"; }
  if (w.querySelectorAll('.ks3-cross-note').length !== 4) {
    return "the lookup table does not carry all four states";
  }
  for (var i = 0; i < sw.length; i++) {
    if (sw[i].getAttribute('aria-pressed') === 'true') { sw[i].click(); }
  }
  if (w.getAttribute('data-state') !== '0-0') {
    return "both switches were pressed off and the state is " + w.getAttribute('data-state');
  }
  var live = w.querySelectorAll('.ks3-cross-note:not([hidden])');
  if (live.length !== 1) {
    return live.length + " state notes are showing at once";
  }
  // ⚠️ THE GATE THE WHOLE BLOCK EXISTS FOR. Both flows stopped, both counts
  // equal — and the OUTWARD bar is still drawn and still reads a real number.
  // A student who watches it disappear here has learnt the one-way picture.
  var out = w.querySelector('[data-fill="out"]');
  var outVal = w.querySelector('[data-bar="out"]');
  if (!out || out.getBoundingClientRect().width < 1) {
    return "with both flows stopped the outward bar has no width";
  }
  if (!outVal || !/[1-9]/.test(outVal.textContent)) {
    return "the outward count reads zero: " + (outVal ? outVal.textContent : "(absent)");
  }
  var inVal = w.querySelector('[data-bar="in"]');
  if (!inVal || inVal.textContent !== outVal.textContent) {
    return "with both flows stopped the two counts are not equal: "
      + (inVal ? inVal.textContent : "(absent)") + " vs " + outVal.textContent;
  }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "a switch was used and the stop did not tick";
  }
  return "";
})()
""",

    # Commits the FIRST part on the FIRST factor and opens it. Whether that
    # pick is right or wrong is the author's business — the reveal opens either
    # way, and the row this drives asserts exactly that.
    "fault-opened": r"""
(function () {
  var sec = document.querySelector('[data-faultblock]');
  if (!sec) { return "no fault-bench on the page"; }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on load";
  }
  var w = sec.querySelector('[data-fault]');
  var tabs = w ? w.querySelectorAll('.ks3-fault-tab') : [];
  if (tabs.length < 2) { return "the bench draws fewer than two factors"; }
  var opts = w.querySelectorAll('.ks3-option');
  if (opts.length < 2) { return "the bench offers fewer than two parts"; }
  var btn = w.querySelector('[data-fault-open]');
  if (!btn) { return "the bench has no reveal button"; }
  if (!btn.disabled) { return "the reveal was open before a part was chosen"; }
  opts[0].click();
  if (btn.disabled) { return "a part was chosen and the reveal is still locked"; }
  btn.click();
  var rev = w.querySelector('.ks3-fault-reveal:not([hidden])');
  if (!rev) { return "the reveal was opened and no panel is showing"; }
  if (w.querySelectorAll('.ks3-fault-reveal:not([hidden])').length !== 1) {
    return "more than one reveal is showing at once";
  }
  // ⚖️ EXACTLY ONE VERDICT, AND THE REVEAL OPENED REGARDLESS. If a future pass
  // ever withholds the explanation from a student who guessed wrong, the
  // headline below goes missing and this fails.
  var verdicts = rev.querySelectorAll('[data-verdict]:not([hidden])');
  if (verdicts.length !== 1) {
    return verdicts.length + " verdict lines are showing; there must be exactly one";
  }
  var answer = rev.querySelector('.ks3-fault-answer');
  if (!answer || !answer.textContent.replace(/\s/g, '')) {
    return "the reveal opened without its answer headline";
  }
  if (!rev.querySelectorAll('.ks3-fault-row').length) {
    return "the reveal opened with no explanation rows";
  }
  var locked = w.querySelectorAll('.ks3-option[disabled]');
  if (locked.length !== opts.length) {
    return "the options did not lock when the factor was opened";
  }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked with only one of the factors opened";
  }
  return "";
})()
""",

    # Drives the light to the compensation point, computing it from the
    # instrument's OWN authored constants rather than from a named preset — so
    # this proves the balanced branch is reachable in a browser whatever the
    # author set the presets to.
    "tpl-balanced": r"""
(function () {
  var sec = document.querySelector('[data-tplblock]');
  if (!sec) { return "no two-process-ledger on the page"; }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on load";
  }
  var w = sec.querySelector('[data-tpl]');
  var slider = w ? w.querySelector('[data-tpl-slider]') : null;
  if (!slider) { return "the ledger has no light slider"; }
  var resp = Number(w.getAttribute('data-resp'));
  var max = Number(w.getAttribute('data-max'));
  var k = Number(w.getAttribute('data-const'));
  var win = Number(w.getAttribute('data-window'));
  var restW = w.querySelector('[data-fill="resp"]').getBoundingClientRect().width;
  var target = null;
  for (var n = 0; n <= 100; n += 1) {
    if (Math.abs(max * (1 - Math.exp(-n / k)) - resp) < win) { target = n; break; }
  }
  if (target === null) {
    return "no light level reaches the balanced window; the branch is unreachable";
  }
  slider.value = target;
  slider.dispatchEvent(new Event('input', {bubbles: true}));
  var fill = w.querySelector('[data-fill="net"]');
  if (!fill || fill.getAttribute('data-tone') !== 'balanced') {
    return "light " + target + " is inside the window and the net bar reads "
      + (fill ? fill.getAttribute('data-tone') : "(absent)");
  }
  var v = w.querySelectorAll('.ks3-tpl-verdict:not([hidden])');
  if (v.length !== 1 || v[0].getAttribute('data-verdict') !== 'balanced') {
    return "the compensation point is showing " + v.length + " verdict(s)";
  }
  // ⚖️ THE BAR THAT NEVER MOVES. Measured at darkness and again at the
  // compensation point. If these ever differ, respiration has acquired a light
  // term and the lesson's whole confrontation is gone.
  var nowW = w.querySelector('[data-fill="resp"]').getBoundingClientRect().width;
  if (Math.abs(nowW - restW) > 0.5) {
    return "the respiration bar moved with the light: " + restW.toFixed(2)
      + "px -> " + nowW.toFixed(2) + "px";
  }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "the light was adjusted and the stop did not tick";
  }
  return "";
})()
""",
    # ═══ END B4 ═══ drives
    # ═══ BEGIN B6 ═══ drives
    #
    # ⚠️ STRUCTURAL, NOT KEYED ON AN AUTHORED ID, for B4's reason: these reach
    # the state they want through the instrument's own controls, by position,
    # so a drive cannot fail as a colour regression on the day an author
    # renames `caffeine` or reorders the drinks.

    # Follows one dose all the way round, one stage at a time — and proves on
    # the way that the route cannot be skipped, that the closing panel cannot
    # arrive early, and that changing drug puts the student back at the start.
    "route-followed": r"""
(function () {
  var sec = document.querySelector('[data-routeblock]');
  if (!sec) { return "no route-tracer on the page"; }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on load";
  }
  var w = sec.querySelector('[data-route]');
  if (!w) { return "the practical shell rendered without the instrument"; }
  var total = parseInt(w.getAttribute('data-total'), 10);
  // ⚖️ FIVE. Stage 3 — once round the whole body — is the block (NOTES-B6
  // §2.1), and a pass that collapses it into stage 2 to save space leaves an
  // instrument that still works and no longer argues anything.
  if (total !== 5) {
    return "the tracer declares " + total + " stages, not five";
  }
  var tabs = w.querySelectorAll('[data-pick]');
  if (tabs.length < 2) { return "the tracer offers fewer than two drugs"; }
  var next = w.querySelector('[data-route-next]');
  var reset = w.querySelector('[data-route-reset]');
  if (!next) { return "the tracer has no advance control"; }
  if (!reset) { return "the tracer has no reset control"; }
  if (w.querySelectorAll('.ks3-route-stepbody:not([hidden])').length) {
    return "a stage body was open before the dose was taken";
  }
  if (w.querySelectorAll('.ks3-route-else:not([hidden])').length) {
    return "the closing panel was open before the route was followed";
  }
  if (w.querySelectorAll('.ks3-route-steps:not([hidden])').length !== 1) {
    return "the tracer opens with more than one drug's stage list showing";
  }

  // ⚖️ CHANGING DRUG RESTARTS THE ROUTE. Done FIRST, so the measured state at
  // the end of this drive is a route followed from its own beginning.
  var second = tabs[1];
  second.click();
  next.click();
  next.click();
  if (w.getAttribute('data-step') !== '2') {
    return "two stages were taken and the tracer reads step "
      + w.getAttribute('data-step');
  }
  tabs[0].click();
  if (w.getAttribute('data-step') !== '0') {
    return "changing drug left the route at stage " + w.getAttribute('data-step');
  }
  if (w.querySelectorAll('.ks3-route-stepbody:not([hidden])').length) {
    return "changing drug left a stage body open";
  }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "changing drug left the stop ticked";
  }

  var live = w.querySelector('.ks3-route-steps:not([hidden])');
  var rows = live.querySelectorAll('.ks3-route-step');
  if (rows.length !== 5) {
    return "the live stage list draws " + rows.length + " rows, not five";
  }
  for (var s = 1; s <= total; s++) {
    next.click();
    var open = live.querySelectorAll('.ks3-route-stepbody:not([hidden])');
    if (open.length !== s) {
      return "at stage " + s + ", " + open.length + " stage bodies are open";
    }
    var cur = live.querySelectorAll('.ks3-route-step[data-state="current"]');
    if (cur.length !== 1 || cur[0].getAttribute('data-step') !== String(s)) {
      return "at stage " + s + " the current row is not row " + s;
    }
    if (s < total && w.querySelectorAll('.ks3-route-else:not([hidden])').length) {
      return "the closing panel opened at stage " + s;
    }
  }
  // ⚠️ STAGES 2 AND 3 ARE TWO STAGES, AND THIS IS WHERE A COLLAPSE SHOWS UP.
  // Nothing can check prose; what can be checked is that the two rows are not
  // the same row twice.
  var t2 = rows[1].querySelector('.ks3-route-steptitle').textContent.trim();
  var t3 = rows[2].querySelector('.ks3-route-steptitle').textContent.trim();
  var b2 = rows[1].querySelector('.ks3-route-stepbody').textContent.trim();
  var b3 = rows[2].querySelector('.ks3-route-stepbody').textContent.trim();
  if (!t3 || !b3) { return "stage 3 arrived with no text"; }
  if (t2 === t3 || b2 === b3) {
    return "stages 2 and 3 have collapsed into one stage";
  }
  var pan = w.querySelectorAll('.ks3-route-else:not([hidden])');
  if (pan.length !== 1) {
    return pan.length + " closing panels are showing; there must be exactly one";
  }
  if (!pan[0].querySelectorAll('.ks3-route-organrow').length) {
    return "the closing panel opened with no organ rows";
  }
  if (!pan[0].querySelector('.ks3-route-verdict')) {
    return "the closing panel opened without its verdict";
  }
  if (!next.disabled) {
    return "the advance control is still live past the last stage";
  }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "the route was followed to the end and the stop did not tick";
  }
  return "";
})()
""",

    # Runs the clock out — and on the way asserts the one thing this block
    # exists to say. Every fix is selected in turn, at rest and again mid-clock,
    # and the hours and the bar are required to be IDENTICAL across all of
    # them. An implementation where any intervention moves the number fails
    # here, on the page, in a browser.
    "clock-run": r"""
(function () {
  var sec = document.querySelector('[data-clearblock]');
  if (!sec) { return "no clearance-clock on the page"; }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on load";
  }
  var w = sec.querySelector('[data-clearance]');
  if (!w) { return "the practical shell rendered without the instrument"; }
  var hoursEl = w.querySelector('[data-clock-hours]');
  var remainEl = w.querySelector('[data-clock-remaining]');
  var fillEl = w.querySelector('[data-clock-fill]');
  var verdict = w.querySelector('[data-clock-verdict]');
  var waitBtn = w.querySelector('[data-clock-wait]');
  var resetBtn = w.querySelector('[data-clock-reset]');
  var fixes = w.querySelectorAll('[data-fix]');
  var drinks = w.querySelectorAll('[data-add]');
  if (!hoursEl || !fillEl || !waitBtn || !resetBtn) {
    return "the bench is missing one of its readouts or controls";
  }
  if (fixes.length < 2) { return "the bench offers fewer than two fixes"; }
  if (!drinks.length) { return "the bench offers nothing to pour"; }
  if (!verdict || !verdict.hasAttribute('hidden')) {
    return "the verdict is showing before the clock was run";
  }
  if (w.querySelectorAll('.ks3-clock-note:not([hidden])').length !== 1) {
    return "the bench opens showing " +
      w.querySelectorAll('.ks3-clock-note:not([hidden])').length + " fix notes";
  }

  // Pour a known evening, so the assertion below is about the fixes and not
  // about whatever the block happened to open on.
  resetBtn.click();
  drinks[0].click();
  drinks[0].click();
  var poured = Number(w.getAttribute('data-units'));
  if (!(poured > 0)) { return "two drinks were poured and the glass reads " + poured; }
  // ⚖️ ONE UNIT, ONE HOUR — asserted against the READOUT, not only against the
  // number of presses it then takes. Halving the printed figure while leaving
  // the model alone passes every other check on this drive and is a lie in the
  // one place a student reads.
  if (!(new RegExp('(^|\\D)' + poured + '(\\D|$)')).test(hoursEl.textContent)) {
    return poured + " units were poured and the clock reads "
      + hoursEl.textContent;
  }

  // ══ THE INSTRUMENT ══ every fix, same evening, same number.
  var seen = {}, bars = {}, n = 0;
  for (var i = 0; i < fixes.length; i++) {
    fixes[i].click();
    if (fixes[i].getAttribute('aria-pressed') !== 'true') {
      return "a fix was chosen and did not light";
    }
    if (w.querySelectorAll('.ks3-clock-note:not([hidden])').length !== 1) {
      return "choosing a fix showed more than one note";
    }
    if (!seen[hoursEl.textContent]) { seen[hoursEl.textContent] = 1; n += 1; }
    bars[fillEl.style.width] = 1;
  }
  if (n !== 1) {
    return "AN INTERVENTION MOVED THE CLOCK: " + Object.keys(seen).join(" / ");
  }
  if (Object.keys(bars).length !== 1) {
    return "an intervention moved the blood bar: " + Object.keys(bars).join(" / ");
  }

  waitBtn.click();
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "an hour was waited and the stop did not tick";
  }
  if (verdict.hasAttribute('hidden')) {
    return "the clock was run and no verdict appeared";
  }
  var mid = {}, m = 0;
  for (var j = 0; j < fixes.length; j++) {
    fixes[j].click();
    var key = remainEl.textContent + "|" + fillEl.style.width;
    if (!mid[key]) { mid[key] = 1; m += 1; }
  }
  if (m !== 1) {
    return "AN INTERVENTION MOVED THE RUNNING CLOCK: " + Object.keys(mid).join(" / ");
  }

  // ⊕ MRB-257 · audit 5.19 — POURING ANOTHER DRINK MUST NOT RESTART THE CLOCK.
  //
  // This drive used to assert the OPPOSITE: `data-hour === '0'` after a pour,
  // defended here as "Design's own `hour: 0`" on the reasoning that leaving
  // the hours alone would credit new units with time that passed before they
  // existed. That reasoning is backwards. The reset zeroed the hours while
  // KEEPING the gross total, so a student who waited two hours and then poured
  // one more unit was shown five units left and no time elapsed — the drink
  // they had already cleared came back. The whole authority of this bench is
  // "one unit an hour, nothing else has a vote", and the reset was the single
  // thing on the page breaking it.
  //
  // The audit rules the reset out, so the gate now pins the RULE rather than
  // the defect, and pins it harder than before: the clock does not move when
  // you pour, what is left is always what you poured less the hours you have
  // waited, and that is asserted against the READOUT as well as the model.
  var hourBefore = Number(w.getAttribute('data-hour'));
  drinks[0].click();
  var hourAfter = Number(w.getAttribute('data-hour'));
  if (hourAfter !== hourBefore) {
    return "pouring another drink moved the elapsed clock from " + hourBefore
      + " to " + hourAfter;
  }
  poured = Number(w.getAttribute('data-units'));

  // What is still in the blood, and what the student is told is still in it.
  var owed = poured - hourAfter;
  if (!(new RegExp('(^|\\D)' + owed + '(\\D|$)')).test(remainEl.textContent)) {
    return "after pouring at hour " + hourAfter + ", " + owed
      + " units should be left and the readout says " + remainEl.textContent;
  }

  // Run it out. The waits left must equal what is owed — never the gross
  // total again, which is what the old assertion was really measuring.
  var hours = 0, guard = 0;
  while (!waitBtn.disabled && guard < 60) { waitBtn.click(); hours += 1; guard += 1; }
  if (hours !== owed) {
    return poured + " units poured at hour " + hourAfter + " took " + hours
      + " hours to clear, not " + owed;
  }
  if (fillEl.getBoundingClientRect().width > 1) {
    return "the blood is clear and the bar still has width";
  }
  if (!verdict.textContent.replace(/\s/g, '')) {
    return "the clock cleared and the verdict is empty";
  }
  if (verdict.textContent.indexOf('{') >= 0) {
    return "the verdict shipped an unfilled placeholder: " + verdict.textContent;
  }
  if (remainEl.textContent.indexOf('{') >= 0 ||
      hoursEl.textContent.indexOf('{') >= 0) {
    return "a readout shipped an unfilled placeholder";
  }
  return "";
})()
""",

    # Commits a DELIBERATELY WRONG fault on the first claim and checks it. The
    # wrong branch is the one a marking colour would appear in first, and it is
    # also where the promise the block makes has to hold: the reveal opens
    # anyway, and it names the right fault in full.
    "claims-checked": r"""
(function () {
  var sec = document.querySelector('[data-ccheckblock]');
  if (!sec) { return "no claim-check on the page"; }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on load";
  }
  var w = sec.querySelector('[data-ccheck]');
  if (!w) { return "the practical shell rendered without the instrument"; }
  var tabs = w.querySelectorAll('[data-pick]');
  var opts = w.querySelectorAll('.ks3-ccheck-fault');
  var panels = w.querySelectorAll('.ks3-ccheck-verdict');
  var btn = w.querySelector('[data-ccheck-open]');
  var tally = w.querySelector('[data-ccheck-tally]');
  if (tabs.length < 2) { return "the bench draws fewer than two claims"; }
  if (opts.length < 2) { return "the bench offers fewer than two faults"; }
  if (!btn) { return "the bench has no check button"; }
  if (!btn.disabled) { return "the check button was live before a fault was picked"; }
  if (w.querySelectorAll('.ks3-ccheck-verdict:not([hidden])').length) {
    return "a verdict is showing before anything was checked";
  }
  if (w.querySelectorAll('.ks3-ccheck-fault[aria-pressed="true"]').length) {
    return "a fault is already chosen on load";
  }

  // ⚖️ THE POOL IS ONE-TO-ONE, AND IT IS CHECKABLE FROM THE DOCUMENT. Every
  // claim names an answer; the answers must be all different and there must be
  // exactly as many faults as claims. A spare fault is an invented distractor
  // and a repeated answer leaves one fault true of nothing on the bench.
  if (panels.length !== tabs.length) {
    return panels.length + " reveal panels for " + tabs.length + " claims";
  }
  if (opts.length !== tabs.length) {
    return opts.length + " faults offered for " + tabs.length +
      " claims; the pool is one-to-one";
  }
  var answers = {}, distinct = 0, ids = {};
  for (var p = 0; p < opts.length; p++) { ids[opts[p].getAttribute('data-fault')] = 1; }
  for (var q = 0; q < panels.length; q++) {
    var ans = panels[q].getAttribute('data-answer');
    if (!ids[ans]) { return "a claim answers " + ans + ", which is not on the bench"; }
    if (!answers[ans]) { answers[ans] = 1; distinct += 1; }
  }
  if (distinct !== panels.length) {
    return "the fault pool is not one-to-one: " + distinct +
      " distinct answers across " + panels.length + " claims";
  }
  // ⚠️ AND EVERY PANEL NAMES ITS OWN ANSWER. Checked across all five rather
  // than on the one the block opens on: an implementation that always prints
  // the first fault in the list is correct for exactly one claim, and the
  // opening claim is the one it happens to be correct for.
  var byId = {};
  for (var t0 = 0; t0 < opts.length; t0++) {
    byId[opts[t0].getAttribute('data-fault')] =
      opts[t0].querySelector('.ks3-ccheck-faulttext').textContent.trim();
  }
  for (var v = 0; v < panels.length; v++) {
    var line = panels[v].querySelector('.ks3-ccheck-answer');
    if (!line) { return "a reveal panel carries no answer line"; }
    if (line.textContent.trim() !== byId[panels[v].getAttribute('data-answer')]) {
      return "claim " + panels[v].getAttribute('data-verdict') +
        " names a fault that is not its answer: " +
        line.textContent.trim().slice(0, 60);
    }
  }

  // Pick a fault that is NOT the answer to the claim showing.
  var live = w.querySelector('.ks3-ccheck-verdict[data-answer]');
  var current = w.getAttribute('data-claim');
  var right = null;
  for (var r = 0; r < panels.length; r++) {
    if (panels[r].getAttribute('data-verdict') === current) {
      right = panels[r].getAttribute('data-answer');
    }
  }
  if (right === null) { return "the opening claim has no reveal panel"; }
  var wrong = null;
  for (var i = 0; i < opts.length; i++) {
    if (opts[i].getAttribute('data-fault') !== right) { wrong = opts[i]; break; }
  }
  if (!wrong) { return "every fault is the answer to the opening claim"; }
  wrong.click();
  if (btn.disabled) { return "a fault was chosen and the check button is still locked"; }
  btn.click();

  var open = w.querySelectorAll('.ks3-ccheck-verdict:not([hidden])');
  if (open.length !== 1) {
    return open.length + " reveals are showing; there must be exactly one";
  }
  var words = open[0].querySelectorAll('[data-word]:not([hidden])');
  if (words.length !== 1) {
    return words.length + " verdict words are showing; there must be exactly one";
  }
  // ⚖️ THE REVEAL IS NOT WITHHELD FOR A WRONG PICK, and it names the RIGHT
  // fault rather than repeating the one that was chosen.
  var named = open[0].querySelector('.ks3-ccheck-answer');
  if (!named || !named.textContent.replace(/\s/g, '')) {
    return "the reveal opened without naming a fault";
  }
  if (named.textContent.trim() ===
      wrong.querySelector('.ks3-ccheck-faulttext').textContent.trim()) {
    return "the reveal named the fault the student picked, not the right one";
  }
  // ⚠️ AND IT NAMED THE RIGHT ONE, not merely a different one. Checking only
  // that it differs from the pick passes an implementation that always prints
  // the first fault in the list — which is correct for exactly one claim and
  // wrong for the other four.
  var rightOpt = w.querySelector('.ks3-ccheck-fault[data-fault="' + right + '"]');
  if (!rightOpt) { return "the claim's own answer is not on the bench"; }
  if (named.textContent.trim() !==
      rightOpt.querySelector('.ks3-ccheck-faulttext').textContent.trim()) {
    return "the reveal named a fault that is not this claim's answer: "
      + named.textContent.trim().slice(0, 60);
  }
  if (!open[0].querySelector('.ks3-ccheck-why') ||
      !open[0].querySelector('.ks3-ccheck-settle')) {
    return "the reveal opened without its reasoning or its settle line";
  }
  // ⚖️ R10 — THE BENCH DOES NOT MARK. Read off every option, in the state a
  // marking colour would appear in first.
  var OK = 'rgb(18, 161, 80)', DANGER = 'rgb(255, 107, 107)';
  for (var o = 0; o < opts.length; o++) {
    var cs = getComputedStyle(opts[o]);
    var mk = getComputedStyle(opts[o].querySelector('.ks3-ccheck-mark'));
    var seen = [cs.color, cs.backgroundColor, cs.borderTopColor,
                mk.color, mk.backgroundColor, mk.borderTopColor];
    for (var c = 0; c < seen.length; c++) {
      if (seen[c] === OK || seen[c] === DANGER) {
        return "THE BENCH IS MARKING: option " + o + " resolved " + seen[c];
      }
    }
    if (/is-correct|is-wrong/.test(opts[o].className)) {
      return "THE BENCH IS MARKING: option " + o + " carries " + opts[o].className;
    }
  }
  if (w.querySelectorAll('.ks3-ccheck-fault:not([disabled])').length) {
    return "the faults did not lock when the claim was checked";
  }
  if (tally && tally.textContent.indexOf('{') >= 0) {
    return "the tally shipped an unfilled placeholder: " + tally.textContent;
  }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked with only one of the claims checked";
  }
  return "";
})()
""",
    # ═══ END B6 ═══ drives

    # ═══ BEGIN B5 ═══ drives
    #
    # ⚠️ STRUCTURAL, NOT KEYED ON AN AUTHORED ID, for B4's and B6's reason:
    # these reach the state they want through the instrument's own controls, by
    # POSITION, so a drive cannot fail as a colour regression on the day an
    # author renames `oviduct` or reorders the specimens.
    #
    # ⚖️ AND ONE DRIVE SERVES FIVE PAGES. `b5-item-checked` is written against
    # the commit chassis rather than against any one lesson, which is what lets
    # b5-01, b5-04, b5-05, b5-06 and b5-08 be measured with the same assertions
    # — the only thing that can see two of them drift apart, which NOTES-B5 §6
    # forbids.

    # Commits a DELIBERATELY WRONG answer on the opening item, checks it, and
    # proves on the way that the reveal is withheld until the commitment, that
    # it opens anyway when the pick was wrong, that the options lock, that the
    # bench does not mark, that a second item is untouched by the first, and
    # that one checked item is not a completed stage.
    "b5-item-checked": r"""
(function () {
  var sec = document.querySelector('[data-b5cblock]');
  if (!sec) { return "no commit bench on the page"; }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on load";
  }
  var w = sec.querySelector('[data-b5c]');
  if (!w) { return "the practical shell rendered without the instrument"; }
  var total = parseInt(w.getAttribute('data-total'), 10);
  var tabs = w.querySelectorAll('[data-b5c-pick]');
  if (!(total > 1) || tabs.length !== total) {
    return "the bench declares " + total + " items and draws " +
      tabs.length + " tabs";
  }
  var btn = w.querySelector('[data-b5c-check]');
  var hint = w.querySelector('[data-b5c-hint]');
  if (!btn) { return "the bench has no check control"; }
  if (!btn.disabled) {
    return "the check button is live before anything has been chosen";
  }

  // ⚖️ ONE ITEM SHOWING, AND ONE ONLY — panel row, option list and reveal.
  // A second visible option list is two benches on top of each other and
  // every pick would land on whichever the wiring found first.
  if (w.querySelectorAll('.ks3-b5c-item:not([hidden])').length !== 1) {
    return "the bench opens with " +
      w.querySelectorAll('.ks3-b5c-item:not([hidden])').length +
      " item panels showing";
  }
  var lists = w.querySelectorAll('.ks3-b5c-opts:not([hidden])');
  if (lists.length !== 1) {
    return "the bench opens with " + lists.length + " option lists showing";
  }
  if (w.querySelectorAll('.ks3-b5c-reveal:not([hidden])').length) {
    return "a reveal was open before anything was checked";
  }
  // ⚠️ AND THEY ARE REALLY HIDDEN, not merely marked hidden — MRB-242, asked
  // of the CASCADE rather than of the painted page.
  //
  // ⚖️ THIS IS WHY THE ORDINARY MRB-242 AUDIT CANNOT SEE THIS COMPONENT, and
  // it is worth writing down. That audit reads computed `display` on the
  // undriven load; `wireB5Commit` draws once on load and `setHidden()` writes
  // an INLINE `display: none`, which masks any author rule underneath it. So
  // a stylesheet that gave `.ks3-b5c-opts` a `display` would ship a page that
  // is correct the instant JS runs and broken before it — eight option lists
  // stacked open for a reader with JS off, and invisible to every gate.
  // Dropping the inline value for the length of one read asks the question
  // the audit means to ask: does the ATTRIBUTE alone still hide it?
  var cascade = w.querySelectorAll(
    '.ks3-b5c-opts[hidden], .ks3-b5c-item[hidden], .ks3-b5c-reveal[hidden]');
  for (var h = 0; h < cascade.length; h++) {
    var el = cascade[h], prev = el.style.display;
    el.style.display = '';
    var shown = getComputedStyle(el).display;
    el.style.display = prev;
    if (shown !== 'none') {
      return "MRB-242: " + el.className + " ships `hidden` but the stylesheet " +
        "gives it display:" + shown + ", which beats the UA [hidden] rule";
    }
  }

  var current = w.getAttribute('data-item');
  var panel = w.querySelector('.ks3-b5c-reveal[data-b5c-reveal="' +
                              current + '"]');
  if (!panel) { return "the opening item has no reveal panel"; }
  var right = panel.getAttribute('data-answer');
  var opts = lists[0].querySelectorAll('.ks3-b5c-opt');
  if (opts.length < 2) {
    return "the opening item offers " + opts.length + " option(s)";
  }
  var wrong = null;
  for (var i = 0; i < opts.length; i++) {
    if (opts[i].getAttribute('data-opt') !== right) { wrong = opts[i]; break; }
  }
  if (!wrong) { return "every option is the answer to the opening item"; }

  wrong.click();
  if (btn.disabled) {
    return "an option was chosen and the check button is still locked";
  }
  if (hint && !hint.textContent.replace(/\s/g, '')) {
    return "the hint went blank once an option was chosen";
  }
  btn.click();

  var open = w.querySelectorAll('.ks3-b5c-reveal:not([hidden])');
  if (open.length !== 1) {
    return open.length + " reveals are showing; there must be exactly one";
  }
  // ⚖️ THE REVEAL IS NOT WITHHELD FOR A WRONG PICK, and it names the answer in
  // full. That is the only thing that makes a wrong guess worth making.
  var words = open[0].querySelectorAll('[data-word]:not([hidden])');
  if (words.length !== 1) {
    return words.length + " verdict words are showing; there must be exactly one";
  }
  if (words[0].getAttribute('data-word') !== 'wrong') {
    return "a deliberately wrong pick was reported as " +
      words[0].getAttribute('data-word');
  }
  var line = open[0].querySelector('.ks3-b5c-answer');
  if (!line || !line.textContent.replace(/\s/g, '')) {
    return "the reveal opened without naming an answer";
  }
  if (!open[0].querySelector('.ks3-b5c-why')) {
    return "the reveal opened without its reasoning";
  }
  if (lists[0].querySelectorAll('.ks3-b5c-opt:not([disabled])').length) {
    return "the options did not lock when the item was checked";
  }

  // ⚖️ R10 — THE BENCH DOES NOT MARK. Read off every option, in the state a
  // marking colour would appear in first: one chosen and wrong, the rest
  // spent. Nothing here may be `--ks3-ok` or `--ks3-danger`, and nothing may
  // carry the ladder's own classes.
  var OK = 'rgb(18, 161, 80)', DANGER = 'rgb(255, 107, 107)';
  for (var o = 0; o < opts.length; o++) {
    var cs = getComputedStyle(opts[o]);
    var mkEl = opts[o].querySelector('.ks3-opt-mark');
    var mk = mkEl ? getComputedStyle(mkEl)
                  : { color: '', backgroundColor: '', borderTopColor: '' };
    var seen = [cs.color, cs.backgroundColor, cs.borderTopColor,
                mk.color, mk.backgroundColor, mk.borderTopColor];
    for (var c = 0; c < seen.length; c++) {
      if (seen[c] === OK || seen[c] === DANGER) {
        return "THE BENCH IS MARKING: option " + o + " resolved " + seen[c];
      }
    }
    if (/is-correct|is-wrong/.test(opts[o].className)) {
      return "THE BENCH IS MARKING: option " + o + " carries " +
        opts[o].className;
    }
  }

  // ⚖️ EVERY ITEM KEEPS ITS OWN PICK AND ITS OWN CHECKED FLAG. A student who
  // checks one and moves on must find the next uncommitted and the first
  // exactly as they left it.
  var second = null;
  for (var s = 0; s < tabs.length; s++) {
    if (tabs[s].getAttribute('data-b5c-pick') !== current) {
      second = tabs[s]; break;
    }
  }
  if (!second) { return "the bench has no second item to switch to"; }
  second.click();
  if (w.querySelectorAll('.ks3-b5c-reveal:not([hidden])').length) {
    return "switching item left a reveal open on the new item";
  }
  if (!btn.disabled) {
    return "switching item left the check button live on an uncommitted item";
  }
  var live = w.querySelectorAll('.ks3-b5c-opts:not([hidden])')[0];
  if (!live) { return "switching item showed no option list"; }
  if (!live.querySelectorAll('.ks3-b5c-opt:not([disabled])').length) {
    return "switching item found the new item's options already locked";
  }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked with only one of " + total + " items checked";
  }
  // Back, so the measured state is the checked item with its reveal open.
  for (var b = 0; b < tabs.length; b++) {
    if (tabs[b].getAttribute('data-b5c-pick') === current) {
      tabs[b].click(); break;
    }
  }
  if (w.querySelectorAll('.ks3-b5c-reveal:not([hidden])').length !== 1) {
    return "coming back to a checked item did not restore its reveal";
  }
  if (w.querySelectorAll('.ks3-b5c-opt[aria-pressed="true"]').length !== 1) {
    return "coming back to a checked item did not restore its pick";
  }
  return "";
})()
""",

    # Opens the first two rows of a comparison table, and proves that the row
    # itself is the control, that the why arrives with it, and that the count
    # does not fall when a row is closed again.
    "b5-rows-opened": r"""
(function () {
  var sec = document.querySelector('[data-cmpblock]');
  if (!sec) { return "no comparison table on the page"; }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on load";
  }
  var w = sec.querySelector('[data-cmprows]');
  if (!w) { return "the practical shell rendered without the instrument"; }
  var total = parseInt(w.getAttribute('data-total'), 10);
  var btns = w.querySelectorAll('[data-cmp-open]');
  if (!(total > 1) || btns.length !== total) {
    return "the table declares " + total + " rows and draws " +
      btns.length + " controls";
  }
  // ⚖️ NOTHING IS OPEN ON LOAD (MRB-208, and NOTES-B5 §2.5's `open: {}`).
  if (w.querySelectorAll('.ks3-cmp-why:not([hidden])').length) {
    return "a why was open before any row was tapped";
  }
  if (w.querySelectorAll('.ks3-cmp-row[data-open]').length) {
    return "a row was tinted open before any row was tapped";
  }
  // ⚖️ THE WHOLE ROW IS THE BUTTON — one control per row, and it is the row.
  // A chevron would be a second control inside it.
  if (w.querySelectorAll('.ks3-cmp-row').length !== total) {
    return "the table draws " + w.querySelectorAll('.ks3-cmp-row').length +
      " rows for " + total + " declared";
  }
  for (var r = 0; r < btns.length; r++) {
    var row = btns[r].closest('.ks3-cmp-row');
    if (!row) { return "a row control is not inside a row"; }
    if (row.querySelectorAll('button').length !== 1) {
      return "row " + r + " carries " +
        row.querySelectorAll('button').length +
        " controls; the whole row is the button (NOTES-B5 §2.5)";
    }
  }

  btns[0].click();
  if (w.querySelectorAll('.ks3-cmp-why:not([hidden])').length !== 1) {
    return "tapping a row opened " +
      w.querySelectorAll('.ks3-cmp-why:not([hidden])').length + " whys";
  }
  var first = btns[0].closest('.ks3-cmp-row');
  if (!first.hasAttribute('data-open')) {
    return "an opened row is not marked open";
  }
  if (btns[0].getAttribute('aria-pressed') !== 'true') {
    return "an opened row's control is not aria-pressed";
  }
  var why = first.querySelector('.ks3-cmp-why');
  if (!why || !why.textContent.replace(/\s/g, '')) {
    return "the row opened with no reasoning in it";
  }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked with one of " + total + " rows opened";
  }

  // ⚠️ THE COUNT IS OF ROWS EVER OPENED. Closing a row must not untick
  // progress — Design's `open` map never deletes a key — or the rail punishes
  // a student for tidying up after themselves.
  btns[1].click();
  btns[1].click();
  if (first.querySelectorAll('.ks3-cmp-why:not([hidden])').length !== 1) {
    return "opening and closing a second row disturbed the first";
  }
  var read = sec.querySelector('[data-count]');
  if (read && /\b0\b/.test(read.textContent)) {
    return "closing a row took the readout back to zero: " + read.textContent;
  }
  return "";
})()
""",

    # Walks the dial: proves the release day MOVES with the length, that it is
    # derived rather than stored, that the stop needs two lengths and not the
    # end of the slider, and that the day is clamped when the cycle shortens.
    "b5-dial-relengthed": r"""
(function () {
  var sec = document.querySelector('[data-dialblock]');
  if (!sec) { return "no cycle dial on the page"; }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on load";
  }
  var w = sec.querySelector('[data-dial]');
  if (!w) { return "the practical shell rendered without the instrument"; }
  var luteal = parseInt(w.getAttribute('data-luteal'), 10);
  var credit = parseInt(w.getAttribute('data-credit'), 10);
  var chips = w.querySelectorAll('[data-dial-len]');
  var slider = w.querySelector('[data-dial-day]');
  var rel = w.querySelector('[data-dial-release]');
  var mark = w.querySelector('[data-dial-marker]');
  var relLabel = w.querySelector('[data-dial-rellabel]');
  var phase = w.querySelector('[data-dial-phaseread]');
  var ovary = w.querySelector('[data-dial-ovary]');
  var uterus = w.querySelector('[data-dial-uterus]');
  var note = w.querySelector('[data-dial-note]');
  if (!(luteal > 0)) { return "the dial declares no luteal phase"; }
  if (chips.length < 2) { return "the dial offers fewer than two lengths"; }
  if (!slider || !rel || !mark) { return "the dial is missing its track controls"; }
  // ⚖️ CREDIT IS TWO OR MORE. One is the length the block opens on, so
  // crediting at one would tick the stop on load (MRB-208).
  if (!(credit >= 2)) {
    return "the dial credits its stop at " + credit + " length(s)";
  }

  function leftOf(el) { return parseFloat(el.style.left); }

  // ⚖️ DERIVED, NOT STORED — and the assertion is arithmetic, not a label
  // match. For every length the dial offers, the release tick must read
  // `length - luteal`. A lookup table of 7 / 14 / 21 would render identically
  // and would teach that day 14 is a fact about people (REPRO-05), which is
  // the misconception this lesson exists to confront.
  var seenLefts = [];
  for (var i = 0; i < chips.length; i++) {
    chips[i].click();
    var len = parseInt(chips[i].getAttribute('data-dial-len'), 10);
    var want = len - luteal;
    var txt = relLabel ? relLabel.textContent : '';
    if (txt.indexOf(String(want)) < 0) {
      return "at " + len + " days the release tick reads \"" + txt +
        "\" and the derived day is " + want;
    }
    if (String(slider.max) !== String(len)) {
      return "at " + len + " days the slider tops out at " + slider.max;
    }
    seenLefts.push(leftOf(rel));
  }
  // ⚖️ AND IT MOVED. Every offered length must put the marker somewhere
  // different, or the block's whole argument is invisible.
  for (var a = 0; a < seenLefts.length; a++) {
    for (var b = a + 1; b < seenLefts.length; b++) {
      if (Math.abs(seenLefts[a] - seenLefts[b]) < 0.5) {
        return "two cycle lengths put the release marker in the same place";
      }
    }
  }

  // ⚠️ THE DAY IS CLAMPED WHEN THE CYCLE SHORTENS. Standing on day 30 of a
  // 35-day cycle and switching to 21 must not leave the marker off its track.
  var longest = chips[0], shortest = chips[0];
  for (var c = 0; c < chips.length; c++) {
    var n = parseInt(chips[c].getAttribute('data-dial-len'), 10);
    if (n > parseInt(longest.getAttribute('data-dial-len'), 10)) { longest = chips[c]; }
    if (n < parseInt(shortest.getAttribute('data-dial-len'), 10)) { shortest = chips[c]; }
  }
  longest.click();
  slider.value = slider.max;
  slider.dispatchEvent(new Event('input', { bubbles: true }));
  shortest.click();
  var shortLen = parseInt(shortest.getAttribute('data-dial-len'), 10);
  if (parseInt(slider.value, 10) > shortLen) {
    return "shortening the cycle left the student on day " + slider.value +
      " of " + shortLen;
  }
  if (leftOf(mark) > 100 || leftOf(mark) < 0) {
    return "the day marker sits at " + leftOf(mark) + "% of its own track";
  }

  // ⚖️ BOTH ORGAN PANELS SAY SOMETHING AT EVERY DAY, and the release day has
  // its own phase. A blank panel reads as the organ having stopped.
  var release = shortLen - luteal;
  slider.value = String(release);
  slider.dispatchEvent(new Event('input', { bubbles: true }));
  if (!phase || !phase.textContent.replace(/\s/g, '')) {
    return "the release day has no phase name";
  }
  if (!ovary || !ovary.textContent.replace(/\s/g, '') ||
      !uterus || !uterus.textContent.replace(/\s/g, '')) {
    return "an organ panel is blank on the release day";
  }
  var atRelease = phase.textContent;
  slider.value = '1';
  slider.dispatchEvent(new Event('input', { bubbles: true }));
  if (phase.textContent === atRelease) {
    return "day 1 and the release day report the same phase: " + atRelease;
  }

  // ⚖️ THE STOP TICKS ON LENGTHS SEEN, NOT ON THE END OF THE SLIDER — and by
  // now every length has been tried, so it must be ticked.
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "every cycle length was tried and the stop did not tick";
  }
  if (note && !note.textContent.replace(/\s/g, '')) {
    return "the note under the panel went blank";
  }
  var read = sec.querySelector('[data-count]');
  if (read && read.textContent.indexOf('{') >= 0) {
    return "the readout shipped an unfilled placeholder: " + read.textContent;
  }
  return "";
})()
""",
    # ═══ END B5 ═══ drives

    # ═══ BEGIN B7 ═══ drives
    #
    # ⚠️ STRUCTURAL, NOT KEYED ON AN AUTHORED ID, for B4's, B5's and B6's
    # reason: each of these reaches the state it wants through the instrument's
    # own controls, BY POSITION, so a drive cannot fail as a colour regression
    # on the day an author renames a dial or reorders the plate. The one
    # exception is `b7-method-flamed`, which has to find the flame — and it
    # finds it through the bench's own `data-conditions`, which is the
    # generator's derivation rather than a name typed here.
    #
    # ⚠️ AND FOUR DRIVES, FOUR PAGES, NOTHING SHARED. B5's one drive served
    # five pages because five of its blocks were the same block; nothing in B7
    # is the same block twice, so a shared drive here would be a coincidence
    # enforced.

    # b7-01. Removes the CARBON DIOXIDE — one dial, so the bench lands on a
    # single-factor branch — then tests the leaf. Proves on the way that the
    # bench opens intact and un-tested, that the verdict is withheld until the
    # test, that the three readouts fall to their own zero strings (which are
    # NOT uniform), that the bench does not mark, that turning a dial afterwards
    # un-tests the leaf without unticking the stop, and that the head readout
    # is a named state rather than a shipped placeholder.
    "b7-leaf-tested": r"""
(function () {
  var sec = document.querySelector('[data-rrblock]');
  if (!sec) { return "no reactant remover on the page"; }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on load";
  }
  var w = sec.querySelector('[data-rr]');
  if (!w) { return "the practical shell rendered without the instrument"; }
  var opts = w.querySelectorAll('.ks3-rr-opt');
  if (opts.length < 4) {
    return "the bench draws " + opts.length + " dial settings";
  }
  // ⚠️ THE CONTROLS ARE SERVER-RENDERED. `check_rail_reachable` reads
  // `class="ks3-option` out of the STATIC html, so a bench whose dials arrive
  // from JavaScript has a rail stop that can never tick and no gate but this
  // one can see it.
  if (!/class="[^"]*\bks3-option\b/.test(sec.innerHTML)) {
    return "the dials are not server-rendered options";
  }
  if (w.querySelectorAll('.ks3-rr-verdict:not([hidden])').length) {
    return "an iodine verdict was open before the leaf was tested";
  }
  // ⚠️ AND THEY ARE REALLY HIDDEN, not merely marked hidden — MRB-242, asked
  // of the CASCADE rather than of the painted page. `wireReactantRemover`
  // draws once on load and `setHidden()` writes an INLINE `display: none`,
  // which masks any author rule underneath it; dropping the inline value for
  // the length of one read asks the question the audit means to ask.
  var cascade = w.querySelectorAll('.ks3-rr-verdict[hidden]');
  for (var h = 0; h < cascade.length; h++) {
    var el = cascade[h], prev = el.style.display;
    el.style.display = '';
    var shown = getComputedStyle(el).display;
    el.style.display = prev;
    if (shown !== 'none') {
      return "MRB-242: " + el.className + " ships `hidden` but the stylesheet " +
        "gives it display:" + shown + ", which beats the UA [hidden] rule";
    }
  }

  // ⚖️ THE BENCH OPENS INTACT — every dial on its first setting, and the rate
  // therefore at its maximum. A bench already in a verdict has answered its
  // own question.
  var rate = w.querySelector('[data-rr-rate]');
  if (!rate || rate.textContent.indexOf('100') !== 0) {
    return "the bench does not open at full rate: " +
      (rate ? rate.textContent : "no rate readout");
  }

  // Remove exactly ONE thing: the first setting anywhere whose factor is zero.
  var zero = null;
  for (var i = 0; i < opts.length; i++) {
    if (parseFloat(opts[i].getAttribute('data-f')) === 0) { zero = opts[i]; break; }
  }
  if (!zero) { return "no dial offers a setting that removes anything"; }
  zero.click();

  var gone = zero.getAttribute('data-dial');
  if (w.querySelectorAll('.ks3-rr-opt[aria-pressed="true"]').length !== 4) {
    return "one dial per setting is not being held after a removal";
  }
  if (rate.textContent.indexOf('0') !== 0) {
    return "one thing was removed and the rate is " + rate.textContent +
      " — rate is the PRODUCT of the four dials, so it must be zero";
  }
  var reads = w.querySelectorAll('[data-rr-readout]');
  for (var r = 0; r < reads.length; r++) {
    var want = reads[r].getAttribute('data-zero');
    if (reads[r].textContent !== want) {
      return "a readout at zero rate reads " + reads[r].textContent +
        " and its authored zero string is " + want;
    }
  }
  var bars = w.querySelectorAll('[data-rr-bar]');
  for (var b = 0; b < bars.length; b++) {
    if (parseFloat(bars[b].style.width) !== 0) {
      return "a readout bar is still drawn at " + bars[b].style.width +
        " with the rate at zero";
    }
  }

  var test = w.querySelector('[data-rr-test]');
  if (!test) { return "the bench has no test control"; }
  test.click();
  var open = w.querySelectorAll('.ks3-rr-verdict:not([hidden])');
  if (open.length !== 1) {
    return open.length + " verdicts are showing; there must be exactly one";
  }
  if (open[0].getAttribute('data-rr-verdict') !== gone) {
    return "one dial was removed and the bench reported branch " +
      open[0].getAttribute('data-rr-verdict') + " rather than " + gone;
  }
  if (open[0].textContent.indexOf('{') >= 0) {
    return "the verdict shipped an unfilled placeholder: " + open[0].textContent;
  }
  // ⚖️ THE BENCH DOES NOT MARK (R10). Nothing here is right or wrong: a
  // student has removed something and is being shown what happened.
  for (var o = 0; o < opts.length; o++) {
    if (/is-correct|is-wrong/.test(opts[o].className)) {
      return "THE BENCH IS MARKING: a dial carries " + opts[o].className;
    }
  }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "the leaf was tested and the stop did not tick";
  }
  // The head readout is a NAMED STATE and the name has to be one the markup
  // declares — `setCountState` silently does nothing for a name it cannot
  // find, so a renamed state would be a readout frozen on "not tested yet".
  var count = sec.querySelector('[data-count]');
  if (count) {
    var after = count.getAttribute('data-state-after');
    if (after === null) { return "the head readout declares no `after` state"; }
    if (count.textContent !== after) {
      return "the leaf was tested and the head readout still reads " +
        count.textContent;
    }
  }

  // Turning a dial afterwards un-tests the leaf — the verdict on screen
  // belonged to the jar as it was — and the stop STAYS ticked, because the
  // student has run the test.
  zero.click();
  var back = null;
  for (var q = 0; q < opts.length; q++) {
    if (opts[q].getAttribute('data-dial') === gone &&
        parseFloat(opts[q].getAttribute('data-f')) !== 0) { back = opts[q]; break; }
  }
  if (back) {
    back.click();
    if (w.querySelectorAll('.ks3-rr-verdict:not([hidden])').length) {
      return "a dial was turned after the test and the old verdict stayed open";
    }
    if (sec.getAttribute('data-stage-done') !== '1') {
      return "turning a dial after the test unticked the stop";
    }
    // Put it back so the measured state is the one the rows describe.
    zero.click();
    w.querySelector('[data-rr-test]').click();
  }
  return "";
})()
""",

    # b7-03. Runs the FULL method first — the bench opens on the good one, which
    # is the opposite of b7-02 — then skips one step and runs it again, so the
    # measured panel is a real fault rather than the fallback. Proves the
    # precedence is read from the page, that the result is withheld until the
    # iodine goes on, that changing a step un-runs it, and that the four-state
    # readout fills its own placeholder.
    "b7-method-run": r"""
(function () {
  var sec = document.querySelector('[data-mbblock]');
  if (!sec) { return "no method breaker on the page"; }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on load";
  }
  var w = sec.querySelector('[data-mb]');
  if (!w) { return "the practical shell rendered without the instrument"; }
  var full, precedence, conditions;
  try {
    full = JSON.parse(w.getAttribute('data-full'));
    precedence = JSON.parse(w.getAttribute('data-precedence'));
    conditions = JSON.parse(w.getAttribute('data-conditions'));
  } catch (x) { return "the bench ships no full method or no precedence"; }
  if (!precedence.length) { return "the bench declares no fault precedence"; }
  if (!/class="[^"]*\bks3-option\b/.test(sec.innerHTML)) {
    return "the steps are not server-rendered options";
  }
  if (w.querySelectorAll('.ks3-mb-verdict:not([hidden])').length) {
    return "a result was open before the iodine was added";
  }
  var cascade = w.querySelectorAll('.ks3-mb-verdict[hidden]');
  for (var h = 0; h < cascade.length; h++) {
    var el = cascade[h], prev = el.style.display;
    el.style.display = '';
    var shown = getComputedStyle(el).display;
    el.style.display = prev;
    if (shown !== 'none') {
      return "MRB-242: " + el.className + " ships `hidden` but the stylesheet " +
        "gives it display:" + shown + ", which beats the UA [hidden] rule";
    }
  }

  // ⚖️ THE BENCH OPENS ON THE GOOD METHOD. Every step is on its `full`
  // setting, which is what makes every verdict a consequence of the student's
  // own choice rather than a repair of somebody else's.
  var key;
  for (key in full) {
    if (!Object.prototype.hasOwnProperty.call(full, key)) { continue; }
    var on = w.querySelector('.ks3-mb-opt[data-step="' + key +
                             '"][aria-pressed="true"]');
    if (!on || on.getAttribute('data-opt') !== full[key]) {
      return "the bench does not open on the full method at step " + key;
    }
  }

  var run = w.querySelector('[data-mb-run]');
  if (!run) { return "the bench has no run control"; }
  run.click();
  var open = w.querySelectorAll('.ks3-mb-verdict:not([hidden])');
  if (open.length !== 1 || open[0].getAttribute('data-mb-verdict') !== 'full') {
    return "running the untouched method did not report the full-method result";
  }
  if (run.disabled !== true) {
    return "the iodine was added and the run button is still live";
  }

  // Now break the LAST fault in the precedence — the least severe one — and
  // run again. Anything earlier would be reported ahead of it, which is the
  // ordering this bench exists to teach.
  var last = precedence[precedence.length - 1];
  var wrong = w.querySelector('.ks3-mb-opt[data-step="' + last +
                              '"][aria-pressed="false"]');
  if (!wrong) { return "the least severe fault " + last + " cannot be chosen"; }
  wrong.click();
  if (w.querySelectorAll('.ks3-mb-verdict:not([hidden])').length) {
    return "a step was changed after the run and the old result stayed open";
  }
  if (run.disabled === true) {
    return "a step was changed after the run and the button stayed spent";
  }
  run.click();
  open = w.querySelectorAll('.ks3-mb-verdict:not([hidden])');
  if (open.length !== 1) {
    return open.length + " results are showing; there must be exactly one";
  }
  if (open[0].getAttribute('data-mb-verdict') !== last) {
    return "step " + last + " was skipped and the bench reported " +
      open[0].getAttribute('data-mb-verdict');
  }
  if (!open[0].querySelector('.ks3-mb-conclude')) {
    return "the result opened without saying what it licenses you to conclude";
  }

  // ⚖️ AND NOW THE ORDERING ITSELF. Break a MORE severe fault as well and the
  // bench must report that one — the least severe is still broken and must not
  // win. This is the assertion that makes `precedence` load-bearing rather than
  // decorative: without it, a bench that reported the last matching fault would
  // pass every other check on this page while teaching that a torn leaf and an
  // undatable result are the same size of mistake.
  var severe = precedence[0];
  var scond = conditions[severe] || [];
  var settable = scond.length > 0;
  for (var sc = 0; sc < scond.length; sc++) {
    if (!w.querySelector('.ks3-mb-opt[data-step="' + scond[sc].step +
                         '"][data-opt="' + scond[sc].is + '"]')) {
      settable = false;
    }
  }
  if (settable) {
    // ⚠️ SET IT THROUGH ITS CONDITION, not through a step id. The most severe
    // fault on this bench is named after an OPTION rather than a step — `heat`
    // is never skipped, it is answered one of two ways — so a drive that
    // looked for `.ks3-mb-opt[data-step="flame"]` would find nothing, skip
    // this whole assertion, and report green. It did, once.
    for (var sd = 0; sd < scond.length; sd++) {
      w.querySelector('.ks3-mb-opt[data-step="' + scond[sd].step +
                      '"][data-opt="' + scond[sd].is + '"]').click();
    }
    run.click();
    open = w.querySelectorAll('.ks3-mb-verdict:not([hidden])');
    if (!open.length || open[0].getAttribute('data-mb-verdict') !== severe) {
      return "two faults were broken and the bench reported " +
        (open.length ? open[0].getAttribute('data-mb-verdict') : "nothing") +
        " rather than the more severe " + severe;
    }
    // Put the bench back where the measured rows expect it: one fault, the
    // least severe, reported.
    w.querySelector('[data-mb-reset]').click();
    wrong.click();
    run.click();
  }
  var opts = w.querySelectorAll('.ks3-mb-opt');
  for (var o = 0; o < opts.length; o++) {
    if (/is-correct|is-wrong/.test(opts[o].className)) {
      return "THE BENCH IS MARKING: a step carries " + opts[o].className;
    }
  }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "the iodine was added and the stop did not tick";
  }
  var count = sec.querySelector('[data-count]');
  if (count && count.textContent.indexOf('{') >= 0) {
    return "the head readout shipped an unfilled placeholder: " +
      count.textContent;
  }
  if (count && count.textContent === count.getAttribute('data-state-idle')) {
    return "the bench has been run and the head readout still says " +
      count.textContent;
  }
  return "";
})()
""",

    # b7-03, the SAFETY branch. Reaches the fire by reading the bench's own
    # `data-conditions` for the one branch whose id is not a step — the
    # generator's derivation, so nothing here types the word `flame` — and
    # setting every step the condition names. That condition includes the
    # ETHANOL step, because skipping the ethanol leaves nothing to catch fire;
    # a drive that only pressed the flame button would measure a data fault
    # while believing it had measured the hazard.
    "b7-method-flamed": r"""
(function () {
  var sec = document.querySelector('[data-mbblock]');
  if (!sec) { return "no method breaker on the page"; }
  var w = sec.querySelector('[data-mb]');
  if (!w) { return "the practical shell rendered without the instrument"; }
  var precedence, conditions, full;
  try {
    precedence = JSON.parse(w.getAttribute('data-precedence'));
    conditions = JSON.parse(w.getAttribute('data-conditions'));
    full = JSON.parse(w.getAttribute('data-full'));
  } catch (x) { return "the bench ships no precedence or conditions"; }

  var safety = null;
  for (var i = 0; i < precedence.length; i++) {
    if (!Object.prototype.hasOwnProperty.call(full, precedence[i])) {
      safety = precedence[i]; break;
    }
  }
  if (!safety) { return "no branch on this bench is a safety branch"; }
  // ⚖️ FIRST IN PRECEDENCE, ALWAYS. A hazard reported after a spoiled pattern
  // teaches that the two are the same size of mistake.
  if (precedence[0] !== safety) {
    return "the safety branch is " + (precedence.indexOf(safety) + 1) +
      "th in precedence; it has to be first";
  }
  var cond = conditions[safety] || [];
  if (cond.length < 2) {
    return "the safety branch's condition names " + cond.length +
      " step(s); it depends on the ethanol step as well as the heat one";
  }
  for (var c = 0; c < cond.length; c++) {
    var btn = w.querySelector('.ks3-mb-opt[data-step="' + cond[c].step +
                              '"][data-opt="' + cond[c].is + '"]');
    if (!btn) { return "the bench cannot be set to " + cond[c].is; }
    btn.click();
  }
  w.querySelector('[data-mb-run]').click();
  var open = w.querySelectorAll('.ks3-mb-verdict:not([hidden])');
  if (open.length !== 1 || open[0].getAttribute('data-mb-verdict') !== safety) {
    return "the ethanol was heated over a flame and the bench reported " +
      (open.length ? open[0].getAttribute('data-mb-verdict') : "nothing");
  }
  if (open[0].getAttribute('data-kind') !== 'safety') {
    return "the safety branch is drawn as an ordinary data fault";
  }
  return "";
})()
""",

    # b7-02's tuner needs no drive — see the rows: the opening leaf already
    # earns a habitat and the verdict is on screen at first paint. What it does
    # need is proof that the OPENING LEAF IS THE BAD ONE and that the oak
    # button changes it, which is the whole lesson, so that lives here and is
    # summoned by the one row measured after a press.
    "b7-oak-pressed": r"""
(function () {
  var sec = document.querySelector('[data-ltblock]');
  if (!sec) { return "no leaf tuner on the page"; }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on load";
  }
  var w = sec.querySelector('[data-lt]');
  if (!w) { return "the practical shell rendered without the instrument"; }
  if (!/class="[^"]*\bks3-option\b/.test(sec.innerHTML)) {
    return "the dials are not server-rendered options — #s-tuner's rail stop " +
      "reads `class=\"ks3-option` out of the STATIC html and could never tick";
  }
  var open = w.querySelectorAll('.ks3-lt-verdict:not([hidden])');
  if (open.length !== 1) {
    return open.length + " habitat verdicts are showing at rest; the tuner " +
      "has no reveal and exactly one is always on screen";
  }
  var first = open[0].getAttribute('data-lt-verdict');

  // ⚖️ THE OPENING LEAF IS DELIBERATELY BAD, and the water readout is what
  // says so: over 150% of an oak leaf, with its bar clamped hard against the
  // end of a track that only reaches 200%.
  var water = w.querySelector('[data-lt-readout="water"]');
  var bar = w.querySelector('[data-lt-bar="water"]');
  if (!water || !bar) { return "the tuner draws no water readout"; }
  var pct = parseFloat(water.textContent);
  if (!(pct > 150)) {
    return "the tuner opens on a leaf losing " + pct + "% of an oak leaf's " +
      "water. The opening leaf is deliberately BAD; a sensible one deletes " +
      "the lesson.";
  }
  // ⊕ MRB-257 · audit 5.52 — THE BAR MUST MOVE WITH THE READOUT.
  //
  // This used to assert `width === 100`, and its own message named the formula
  // it was pinning: "the percentage HALVED and clamped at 100". That formula
  // saturates at every value above 200%, and the opening leaf is above 300% —
  // so the readout could fall from 363% to 242% with the bar pinned flat
  // against the end of the track at both ends. A control with no visible
  // effect on the graphic it drives is the defect, and the gate was holding it
  // in place. It now pins the fix: the bar keeps headroom, so a worse leaf has
  // somewhere to draw. (The opening leaf is still deliberately bad — that is
  // the `pct > 150` assertion above, which has not moved.)
  var barOpen = parseFloat(bar.style.width);
  if (!(barOpen > 0 && barOpen < 100)) {
    return "the water bar is drawn at " + bar.style.width + " at " + pct +
      "% — it must keep headroom, or a worse leaf cannot draw any differently";
  }
  var count = sec.querySelector('[data-count]');
  if (count && count.textContent !== count.getAttribute('data-zero')) {
    return "nothing has been touched and the counter reads " + count.textContent;
  }

  var oak = w.querySelector('[data-lt-oak]');
  if (!oak) { return "the tuner has no oak shortcut"; }
  oak.click();
  open = w.querySelectorAll('.ks3-lt-verdict:not([hidden])');
  if (open.length !== 1) {
    return open.length + " habitat verdicts are showing after the oak button";
  }
  if (open[0].getAttribute('data-lt-verdict') === first) {
    return "the oak button left the leaf in the same habitat (" + first +
      "), so pressing it reveals nothing";
  }

  // ⊕ MRB-257 · audit 5.52 — and the bar TRACKED it. The oak leaf is the
  // sensible one, so water loss falls; a readout that falls while the bar
  // stands still is exactly the defect above, caught from the other end. One
  // assertion each way costs nothing and pins a re-clamp at either extreme.
  var pctOak = parseFloat(water.textContent);
  var barOak = parseFloat(bar.style.width);
  if (!(pctOak < pct)) {
    return "the oak button left water loss at " + pctOak + "%, up from " + pct + "%";
  }
  if (!(barOak < barOpen)) {
    return "water loss fell from " + pct + "% to " + pctOak +
      "% and the bar did not follow: " + barOpen + "% then " + barOak + "%";
  }
  if (count) {
    if (count.textContent === count.getAttribute('data-zero')) {
      return "the oak button was pressed and the counter still says nothing " +
        "has changed";
    }
    if (count.textContent.indexOf('{') >= 0) {
      return "the counter shipped an unfilled placeholder: " + count.textContent;
    }
  }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "a dial was moved and the stop did not tick";
  }
  // ⚖️ AND `Start again` DOES NOT UNTICK IT. Design's own predicate is
  // `s.moved`, which her reset clears — so her rail stop unticks when a
  // student tidies up after themselves. MRB-208 ruled the rail records
  // participation, and B5's compare rows count rows EVER opened for the same
  // reason: `everMoved` drives the stop, `moved` drives Design's counter.
  var reset = w.querySelector('[data-lt-reset]');
  if (reset) {
    reset.click();
    if (sec.getAttribute('data-stage-done') !== '1') {
      return "starting again unticked a stop the student had already reached";
    }
    if (count && count.textContent !== count.getAttribute('data-zero')) {
      return "starting again left the counter reading " + count.textContent;
    }
    oak.click();
  }
  return "";
})()
""",

    # b7-04. Walks the opening food's chain to its producer one press at a
    # time, proving that the verdict is withheld until the chain is complete,
    # that each press reveals exactly one more note, that the counter's
    # denominator is THIS food's chain length, and that switching food
    # afterwards restarts the chain without untelling what has been reached.

    # ── B9 · Ecosystems and interdependence (⊕ MRB-250) ──
    #
    # Eight states that exist only after a student does something. Each is
    # reached the way a student reaches it — through the instrument's own
    # control — so a regression in the interaction path fails HERE rather than
    # being measured around. Each also carries the BEHAVIOURAL assertions for
    # its instrument, because a drive that only clicks is a drive that cannot
    # fail for the right reason.

    # b9-01. Climbs the opening chain to the top, proving the verdict is
    # withheld until the chain is complete, that the computed figures are the
    # chain's own, that the denominator follows the tab across chains of
    # different lengths, and that going back to the producers does not untell
    # what has been reached.
    "b9-chain-topped": r"""
(function () {
  var sec = document.querySelector('[data-clblock]');
  if (!sec) { return "no chain ledger on the page"; }
  if (sec.getAttribute('data-stage-done') === '1') { return "the stop ticked on load"; }
  var w = sec.querySelector('[data-cl]');
  if (!w) { return "the practical shell rendered without the instrument"; }
  var tabs = w.querySelectorAll('[data-cl-chain]');
  if (tabs.length < 2) { return "the bench offers " + tabs.length + " chain(s)"; }
  if (!/class="[^"]*\bks3-option\b/.test(sec.innerHTML)) {
    return "the chain tabs are not server-rendered options";
  }
  var count = sec.querySelector('[data-count]');
  if (count && count.textContent.indexOf('{') >= 0) {
    return "the head readout shipped an unfilled placeholder: " + count.textContent;
  }
  var cascade = w.querySelectorAll(
    '[data-cl-chainpanel][hidden], [data-cl-readout][hidden], .ks3-cl-verdict[hidden]');
  for (var h = 0; h < cascade.length; h++) {
    var el = cascade[h], prev = el.style.display;
    el.style.display = '';
    var shown = getComputedStyle(el).display;
    el.style.display = prev;
    if (shown !== 'none') {
      return "MRB-242: " + el.className + " ships `hidden` but the stylesheet " +
        "gives it display:" + shown + ", which beats the UA [hidden] rule";
    }
  }
  var panels = w.querySelectorAll('[data-cl-chainpanel]:not([hidden])');
  if (panels.length !== 1) {
    return "the bench opens with " + panels.length + " chain panels showing";
  }
  var panel = panels[0];
  var total = parseInt(panel.getAttribute('data-total'), 10);
  if (!(total >= 3)) { return "the opening chain has " + total + " level(s)"; }
  if (panel.querySelectorAll('[data-cl-readout]:not([hidden])').length !== 1) {
    return "the chain opens with more than the producer revealed";
  }
  if (w.querySelector('.ks3-cl-verdict:not([hidden])')) {
    return "the verdict landed before the chain was complete";
  }
  // ⚖️ THE PRODUCER IS AT THE BOTTOM. Asserted on painted geometry, not on the
  // stylesheet: `data-i="0"` is the first child in the document and must be
  // the LOWEST on screen. This is the direction-of-energy claim `#s-think`
  // spends a paragraph on.
  var rows = panel.querySelectorAll('.ks3-cl-level');
  if (rows[0].getBoundingClientRect().top <=
      rows[rows.length - 1].getBoundingClientRect().top) {
    return "the producer is not drawn at the bottom of the chain";
  }
  var up = w.querySelector('[data-cl-up]');
  for (var i = 1; i < total; i++) {
    if (up.disabled) { return "the step button locked at level " + i; }
    up.click();
    var shownNow = panel.querySelectorAll('[data-cl-readout]:not([hidden])').length;
    if (shownNow !== i + 1) {
      return "press " + i + " revealed " + shownNow + " level(s); each press reveals one";
    }
    if (i < total - 1 && w.querySelector('.ks3-cl-verdict:not([hidden])')) {
      return "the verdict landed at level " + (i + 1) + " of " + total;
    }
  }
  var verdict = w.querySelector('.ks3-cl-verdict:not([hidden])');
  if (!verdict) { return "the chain reached its top and no verdict landed"; }
  if (verdict.textContent.indexOf('{') >= 0) {
    return "the verdict shipped an unfilled placeholder: " + verdict.textContent;
  }
  if (!up.disabled) { return "the chain is complete and the step button is still live"; }
  // ⚖️ THE TROPHIC ARITHMETIC, READ OFF THE PAGE. A four-level chain at a
  // tenth per step arrives at 0.1% of the original and a five-level chain at
  // 0.01%. If this ever stops holding, B9 has stopped owning the 10:1 that
  // every later lesson cites it for.
  var want4 = { 4: '0.1%', 5: '0.01%', 3: '1%' };
  if (want4[total] && verdict.textContent.indexOf(want4[total]) < 0) {
    return "a " + total + "-level chain reported " + verdict.textContent;
  }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "a chain was climbed to the top and the stop did not tick";
  }
  if (count && count.getAttribute('data-total') !== String(total)) {
    return "the head readout's denominator is " + count.getAttribute('data-total') +
      " and this chain has " + total + " levels";
  }
  // ⚖️ SWITCHING CHAIN RESTARTS THE CLIMB AND UNTELLS NOTHING, and the
  // denominator follows the tab — the chains are deliberately different
  // lengths, which is the argument.
  for (var q = 0; q < tabs.length; q++) {
    if (tabs[q].getAttribute('aria-pressed') === 'false') {
      tabs[q].click();
      var next = w.querySelector('[data-cl-chainpanel]:not([hidden])');
      if (!next) { return "switching chain left no panel showing"; }
      if (next.querySelectorAll('[data-cl-readout]:not([hidden])').length !== 1) {
        return "switching chain did not restart the climb";
      }
      if (count && count.getAttribute('data-total') !==
          next.getAttribute('data-total')) {
        return "the head readout's denominator did not follow the tab";
      }
      if (sec.getAttribute('data-stage-done') !== '1') {
        return "switching chain unticked a stop the student had reached";
      }
      break;
    }
  }
  // ⚖️ AND `Back to the producers` DOES NOT UNTICK IT EITHER. MRB-208 ruled
  // the rail records participation; a student who tidies up after themselves
  // has still climbed the chain.
  var reset = w.querySelector('[data-cl-reset]');
  if (reset) {
    reset.click();
    if (sec.getAttribute('data-stage-done') !== '1') {
      return "going back to the producers unticked a stop already reached";
    }
    if (w.querySelector('.ks3-cl-verdict:not([hidden])')) {
      return "the verdict survived a reset";
    }
  }
  // Leave the bench TOPPED, on the opening chain, for the driven rows.
  tabs[0].click();
  var t = parseInt(
    w.querySelector('[data-cl-chainpanel]:not([hidden])').getAttribute('data-total'), 10);
  for (var z = 1; z < t; z++) { w.querySelector('[data-cl-up]').click(); }
  return "";
})()
""",

    # b9-02. Removes the foxes and runs thirty years, which is the ONE state
    # the carrying-capacity argument can be read in — and the state a model
    # with K dropped would fail in, by climbing for ever.
    "b9-cycle-culled": r"""
(function () {
  var sec = document.querySelector('[data-cyblock]');
  if (!sec) { return "no cycle runner on the page"; }
  if (sec.getAttribute('data-stage-done') === '1') { return "the stop ticked on load"; }
  var w = sec.querySelector('[data-cy]');
  if (!w) { return "the practical shell rendered without the instrument"; }
  var count = sec.querySelector('[data-count]');
  if (count && count.textContent.indexOf('{') >= 0) {
    return "the head readout shipped an unfilled placeholder: " + count.textContent;
  }
  var M;
  try { M = JSON.parse(w.getAttribute('data-model')); }
  catch (x) { return "the model did not parse"; }
  if (!(M.k > 0)) { return "K is " + M.k + " — the grass supply is gone"; }
  if (w.querySelectorAll('.ks3-cy-year').length !== 1) {
    return "the field opens with " + w.querySelectorAll('.ks3-cy-year').length +
      " years of history; it opens with one";
  }
  var prey0 = parseInt(w.querySelector('[data-cy-prey]').textContent, 10);
  var pred0 = parseInt(w.querySelector('[data-cy-pred]').textContent, 10);
  if (!(prey0 > 0 && pred0 > 0)) { return "the field opens empty"; }

  // ⚖️ THE LAG, MEASURED. Run forty years and find each series' peak year in
  // the history. The predator peak must come AFTER the prey peak — that is the
  // entire lesson, it is what both marked rungs test, and it is the first
  // thing a "simplified" model would lose.
  var ten = w.querySelector('[data-cy-ten]');
  for (var i = 0; i < 4; i++) { ten.click(); }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "ten years were run and the stop did not tick";
  }
  var cols = w.querySelectorAll('.ks3-cy-year');
  if (cols.length > M.history) {
    return "the chart holds " + cols.length + " years against a window of " + M.history;
  }
  var bestPrey = -1, bestPred = -1, hiPrey = -1, hiPred = -1, j;
  for (j = 0; j < cols.length; j++) {
    var p = parseFloat(cols[j].querySelector('[data-series="prey"]').style.height);
    var q = parseFloat(cols[j].querySelector('[data-series="pred"]').style.height);
    if (p > hiPrey) { hiPrey = p; bestPrey = j; }
    if (q > hiPred) { hiPred = q; bestPred = j; }
  }
  if (!(bestPred > bestPrey)) {
    return "the predator peak (year index " + bestPred + ") does not follow the " +
      "prey peak (" + bestPrey + ") — the lag is the lesson";
  }
  // ⚖️ AND THE TWO SERIES ARE SCALED SEPARATELY, which the caption says in
  // words. On a shared scale the fox series would never reach the top of the
  // band; each must have its own 100%.
  if (!(hiPrey > 99 && hiPred > 99)) {
    return "the two series are on one scale — tallest prey " + hiPrey +
      "%, tallest predator " + hiPred + "%";
  }

  // ⚖️ K IS THE GRASS SUPPLY. Remove every fox, run thirty more years, and the
  // rabbits must STOP at the ceiling rather than climb without limit — which
  // is the misconception `#s-think` exists to break.
  var cull = w.querySelector('[data-cy-cull]');
  var before = cull.textContent;
  cull.click();
  if (cull.textContent === before) {
    return "removing the foxes did not change the control's label";
  }
  for (var k = 0; k < 3; k++) { ten.click(); }
  var pred = parseInt(w.querySelector('[data-cy-pred]').textContent, 10);
  if (pred !== 0) { return "the foxes were removed and " + pred + " remain"; }
  var prey = parseInt(w.querySelector('[data-cy-prey]').textContent, 10);
  if (prey > M.k * M.prey_cap_mult + 1) {
    return "the rabbits reached " + prey + " against a carrying capacity of " +
      M.k + " — the logistic term is gone and the bench is teaching " +
      "exponential growth";
  }
  if (prey < M.k * 0.9) {
    return "the rabbits reached only " + prey + " of a possible " + M.k +
      " with no predators; the ceiling note can never fire";
  }
  var note = w.querySelector('[data-cy-note]').textContent;
  if (!note) { return "the field is at its ceiling and the note is blank"; }
  if (note.indexOf('{') >= 0) { return "the note shipped a placeholder: " + note; }
  var reset = w.querySelector('[data-cy-reset]');
  if (reset) {
    reset.click();
    if (sec.getAttribute('data-stage-done') !== '1') {
      return "resetting the field unticked a stop already reached";
    }
    // Back to the driven state for the rows.
    w.querySelector('[data-cy-cull]').click();
    for (var z = 0; z < 3; z++) { w.querySelector('[data-cy-ten]').click(); }
  }
  return "";
})()
""",

    # b9-03. Follows the opening removal to round three, proving the verdict is
    # withheld until it gets there, that every species carries exactly three
    # rounds and no empty fourth, and that switching species restarts the
    # count without untelling what has been reached.
    "b9-web-followed": r"""
(function () {
  var sec = document.querySelector('[data-rsblock]');
  if (!sec) { return "no removal bench on the page"; }
  if (sec.getAttribute('data-stage-done') === '1') { return "the stop ticked on load"; }
  var w = sec.querySelector('[data-rs]');
  if (!w) { return "the practical shell rendered without the instrument"; }
  var count = sec.querySelector('[data-count]');
  if (count && count.textContent.indexOf('{') >= 0) {
    return "the head readout shipped an unfilled placeholder: " + count.textContent;
  }
  if (w.querySelectorAll('.ks3-rs-webline').length < 6) {
    return "the web has " + w.querySelectorAll('.ks3-rs-webline').length + " lines";
  }
  // ⚠️ MRB-242 — AN AUTHOR `display` BEATS THE UA `[hidden]` RULE regardless of
  // specificity, and the element then ships visible with the attribute still on
  // it. Nine builds have paid for this. Probed rather than trusted: unset the
  // inline display, read what the STYLESHEET resolves to, put it back.
  var cascade = w.querySelectorAll(
    '[data-rs-panel][hidden], .ks3-rs-roundbody[hidden], .ks3-rs-verdict[hidden]');
  for (var h = 0; h < cascade.length; h++) {
    var cel = cascade[h], cprev = cel.style.display;
    cel.style.display = '';
    var cshown = getComputedStyle(cel).display;
    cel.style.display = cprev;
    if (cshown !== 'none') {
      return "MRB-242: " + cel.className + " ships `hidden` but the stylesheet " +
        "gives it display:" + cshown + ", which beats the UA [hidden] rule";
    }
  }
  var panels = w.querySelectorAll('[data-rs-panel]');
  if (panels.length < 4) { return "the bench offers " + panels.length + " removals"; }
  // ⚠️ EXACTLY THREE ROUNDS ON EVERY SPECIES, AND NO EMPTY FOURTH. Design's
  // `caterpillars` carries `{ title: '', body: '' }` and filters it at draw
  // time; this port has no filter and refuses the entry at build time. If one
  // ever arrives it draws a numbered row with nothing in it, and the counter
  // says "of 4".
  for (var i = 0; i < panels.length; i++) {
    var rounds = panels[i].querySelectorAll('.ks3-rs-round');
    if (rounds.length !== 3) {
      return panels[i].getAttribute('data-rs-panel') + " has " + rounds.length +
        " rounds; every removal has three";
    }
    for (var j = 0; j < rounds.length; j++) {
      if (!rounds[j].querySelector('.ks3-rs-roundtitle').textContent.trim() ||
          !rounds[j].querySelector('.ks3-rs-roundbody').textContent.trim()) {
        return panels[i].getAttribute('data-rs-panel') + " round " + (j + 1) +
          " is empty — an editing artefact reached the page";
      }
    }
  }
  if (w.querySelectorAll('[data-rs-panel]:not([hidden])').length !== 1) {
    return "the bench opens with more than one removal showing";
  }
  var panel = w.querySelector('[data-rs-panel]:not([hidden])');
  if (panel.querySelectorAll('.ks3-rs-roundbody:not([hidden])').length !== 0) {
    return "a consequence was revealed before anything was removed";
  }
  if (panel.querySelector('[data-rs-verdict]:not([hidden])')) {
    return "the verdict landed before the removal was followed";
  }
  var head0 = panel.querySelector('[data-rs-headline]').textContent;
  if (head0.indexOf('{name}') >= 0) {
    return "the headline shipped an unfilled placeholder: " + head0;
  }
  var next = w.querySelector('[data-rs-next]');
  for (var r = 1; r <= 3; r++) {
    if (next.disabled) { return "the step button locked at round " + r; }
    next.click();
    var open = panel.querySelectorAll('.ks3-rs-roundbody:not([hidden])').length;
    if (open !== r) {
      return "press " + r + " revealed " + open + " consequence(s); each press reveals one";
    }
    if (r < 3 && panel.querySelector('[data-rs-verdict]:not([hidden])')) {
      return "the verdict landed at round " + r + " of 3";
    }
  }
  var head1 = panel.querySelector('[data-rs-headline]').textContent;
  if (head1 === head0) { return "the headline did not change when the species was removed"; }
  if (head1.indexOf('{name}') >= 0) {
    return "the removed headline shipped a placeholder: " + head1;
  }
  var verdict = panel.querySelector('[data-rs-verdict]:not([hidden])');
  if (!verdict) { return "three rounds were followed and no verdict landed"; }
  if (!next.disabled) { return "the removal is followed and the step button is still live"; }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "a removal was followed to the end and the stop did not tick";
  }
  var tabs = w.querySelectorAll('[data-rs-species]');
  for (var q = 0; q < tabs.length; q++) {
    if (tabs[q].getAttribute('aria-pressed') === 'false') {
      tabs[q].click();
      var nx = w.querySelector('[data-rs-panel]:not([hidden])');
      if (nx.querySelectorAll('.ks3-rs-roundbody:not([hidden])').length !== 0) {
        return "switching species did not put the wood back";
      }
      if (sec.getAttribute('data-stage-done') !== '1') {
        return "switching species unticked a stop the student had reached";
      }
      break;
    }
  }
  // Back to a FOLLOWED state on the opening species for the driven rows.
  tabs[0].click();
  for (var z = 0; z < 3; z++) { w.querySelector('[data-rs-next]').click(); }
  return "";
})()
""",

    # b9-04. Empties the shelf, which is where the whole lesson is: two bars,
    # two different percentages, and a GAP between them that must survive a
    # phone-width container.
    "b9-shelf-emptied": r"""
(function () {
  var sec = document.querySelector('[data-ssblock]');
  if (!sec) { return "no shelf on the page"; }
  if (sec.getAttribute('data-stage-done') === '1') { return "the stop ticked on load"; }
  var w = sec.querySelector('[data-ss]');
  if (!w) { return "the practical shell rendered without the instrument"; }
  var count = sec.querySelector('[data-count]');
  if (count && count.textContent.indexOf('{') >= 0) {
    return "the head readout shipped an unfilled placeholder: " + count.textContent;
  }
  var bars = w.querySelectorAll('[data-ss-bar]');
  if (bars.length !== 2) { return "the shelf draws " + bars.length + " bars; there are two"; }
  var tiles = w.querySelectorAll('[data-ss-food]');
  if (tiles.length < 8) { return "the shelf stocks " + tiles.length + " foods"; }
  if (w.querySelectorAll('[data-ss-food][data-gone]').length) {
    return "a crop had already failed before the pollinators were removed";
  }
  // ⚖️ AT FULL POLLINATION THE TILE READS `how`, NOT A STATUS — the dial
  // doubles as the teaching label.
  var how0 = tiles[0].querySelector('[data-ss-status]').textContent;
  if (how0 !== tiles[0].getAttribute('data-how')) {
    return "the intact shelf shows a status instead of how the crop is pollinated";
  }
  function pct(i) {
    return parseInt(bars[i].querySelector('[data-ss-value]').textContent, 10);
  }
  if (pct(0) !== 100 || pct(1) !== 100) {
    return "the intact shelf reads " + pct(0) + "% and " + pct(1) + "%";
  }
  var toggle = w.querySelector('[data-ss-toggle]');
  var before = toggle.textContent;
  toggle.click();
  if (toggle.textContent === before) {
    return "removing the pollinators did not change the control's label";
  }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "the pollinators were removed and the stop did not tick";
  }
  var cal = pct(0), vit = pct(1);
  // ⚖️⚖️ THE GAP IS THE ENTIRE LESSON. Calories must survive better than
  // vitamins, and the two must not agree — the note reads the difference
  // aloud and rung 2 marks a student for knowing which falls further.
  if (cal === vit) {
    return "both bars land on " + cal + "% — two bars that agree are one bar drawn twice";
  }
  if (!(cal > vit)) {
    return "calories fell to " + cal + "% and vitamins to " + vit +
      "%; the unit's claim is that the VARIETY goes first";
  }
  var note = w.querySelector('[data-ss-note]').textContent;
  if (note.indexOf('{') >= 0) { return "the note shipped a placeholder: " + note; }
  if (note.indexOf(String(cal)) < 0 || note.indexOf(String(vit)) < 0) {
    return "the note does not quote the two figures beside it: " + note;
  }
  if (!w.querySelectorAll('[data-ss-food][data-gone]').length) {
    return "the pollinators are gone and no crop failed";
  }
  // ⚖️ AND THE TWO BARS SURVIVE A PHONE. The grid is `auto-fit` on the
  // CONTAINER, not on a media query, so squeezing the container is the honest
  // test: they must WRAP to two rows, both still painted, never merge and
  // never drop one.
  var wrap = w.querySelector('.ks3-ss-bars');
  var prev = wrap.style.width;
  wrap.style.width = '260px';
  void wrap.offsetHeight;
  var r0 = bars[0].getBoundingClientRect(), r1 = bars[1].getBoundingClientRect();
  var cols = getComputedStyle(wrap).gridTemplateColumns.split(' ').length;
  var vis = getComputedStyle(bars[0]).display !== 'none' &&
            getComputedStyle(bars[1]).display !== 'none';
  wrap.style.width = prev;
  void wrap.offsetHeight;
  if (cols !== 1) {
    return "squeezed to 260px the bar grid still reports " + cols +
      " tracks; it must wrap to one column";
  }
  if (!(r1.top > r0.top) || !vis || r0.width <= 0 || r1.width <= 0) {
    return "squeezed to a phone width the two bars merged or one was dropped";
  }
  return "";
})()
""",

    # b9-05. Climbs the persistent chemical to the ospreys — the one state
    # where the harm threshold is crossed and the multiplier is quoted.
    "b9-chain-poisoned": r"""
(function () {
  var sec = document.querySelector('[data-bablock]');
  if (!sec) { return "no bioaccumulation bench on the page"; }
  if (sec.getAttribute('data-stage-done') === '1') { return "the stop ticked on load"; }
  var w = sec.querySelector('[data-ba]');
  if (!w) { return "the practical shell rendered without the instrument"; }
  var count = sec.querySelector('[data-count]');
  if (count && count.textContent.indexOf('{') >= 0) {
    return "the head readout shipped an unfilled placeholder: " + count.textContent;
  }
  var tabs = w.querySelectorAll('[data-ba-chem]');
  if (tabs.length < 3) { return "the dial offers " + tabs.length + " settings"; }
  // ⚖️ EXACTLY ONE ×1 SETTING, AND IT IS THE CONTROL.
  var ones = 0, i;
  for (i = 0; i < tabs.length; i++) {
    if (parseFloat(tabs[i].getAttribute('data-factor')) === 1) { ones += 1; }
  }
  if (ones !== 1) {
    return "the dial has " + ones + " settings at ×1; exactly one is the control";
  }
  var levels = w.querySelectorAll('.ks3-ba-level');
  if (levels.length < 4) { return "the chain has " + levels.length + " levels"; }
  // ⚠️ MRB-242 — AN AUTHOR `display` BEATS THE UA `[hidden]` RULE regardless of
  // specificity, and the element then ships visible with the attribute still on
  // it. Nine builds have paid for this. Probed rather than trusted: unset the
  // inline display, read what the STYLESHEET resolves to, put it back.
  var cascade = w.querySelectorAll(
    '.ks3-ba-readout[hidden], .ks3-ba-verdict[hidden]');
  for (var h = 0; h < cascade.length; h++) {
    var cel = cascade[h], cprev = cel.style.display;
    cel.style.display = '';
    var cshown = getComputedStyle(cel).display;
    cel.style.display = cprev;
    if (cshown !== 'none') {
      return "MRB-242: " + cel.className + " ships `hidden` but the stylesheet " +
        "gives it display:" + cshown + ", which beats the UA [hidden] rule";
    }
  }
  if (w.querySelectorAll('.ks3-ba-readout:not([hidden])').length !== 1) {
    return "the chain opens with more than the lake water revealed";
  }
  if (w.querySelector('.ks3-ba-verdict:not([hidden])')) {
    return "the verdict landed before the chain was climbed";
  }
  // The lake water must be at the bottom, as in b9-01.
  if (levels[0].getBoundingClientRect().top <=
      levels[levels.length - 1].getBoundingClientRect().top) {
    return "the lake water is not drawn at the bottom of the chain";
  }
  tabs[0].click();
  var up = w.querySelector('[data-ba-up]');
  for (i = 1; i < levels.length; i++) {
    if (up.disabled) { return "the step button locked at level " + i; }
    up.click();
  }
  if (!up.disabled) { return "the chain is complete and the step button is still live"; }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "the chain was climbed and the stop did not tick";
  }
  var harmful = w.querySelectorAll('.ks3-ba-level[data-harmful]').length;
  if (!harmful) {
    return "the most persistent setting reached the top and nothing is flagged " +
      "as harmful — the lesson's consequence is unreachable";
  }
  var verdict = w.querySelector('.ks3-ba-verdict:not([hidden])');
  if (!verdict) { return "the chain reached the ospreys and no verdict landed"; }
  if (verdict.textContent.indexOf('{') >= 0) {
    return "the verdict shipped an unfilled placeholder: " + verdict.textContent;
  }
  // ⚖️ THE MULTIPLIER IS COMPUTED AND IT IS GROUPED BY HAND, never by
  // `toLocaleString()` — a European locale would print 100,000 as 100.000.
  if (!/[0-9],[0-9]{3}/.test(verdict.textContent) &&
      !/\b\d{1,3}\b/.test(verdict.textContent)) {
    return "the harmful verdict quotes no multiplier: " + verdict.textContent;
  }
  var top = w.querySelectorAll('[data-ba-ppm]');
  var topText = top[top.length - 1].textContent;
  if (!/[0-9]/.test(topText)) { return "the top level prints no concentration"; }
  var reset = w.querySelector('[data-ba-reset]');
  if (reset) {
    reset.click();
    if (sec.getAttribute('data-stage-done') !== '1') {
      return "going back to the water unticked a stop already reached";
    }
    for (i = 1; i < levels.length; i++) { w.querySelector('[data-ba-up]').click(); }
  }
  return "";
})()
""",

    # b9-05 again, on the CONTROL. Its own drive rather than a branch of the
    # one above, because a control measured in the same document as the
    # treatment is not a control.
    "b9-chem-control": r"""
(function () {
  var sec = document.querySelector('[data-bablock]');
  if (!sec) { return "no bioaccumulation bench on the page"; }
  var w = sec.querySelector('[data-ba]');
  if (!w) { return "the practical shell rendered without the instrument"; }
  var tabs = w.querySelectorAll('[data-ba-chem]');
  var ctrl = null, i;
  for (i = 0; i < tabs.length; i++) {
    if (parseFloat(tabs[i].getAttribute('data-factor')) === 1) { ctrl = tabs[i]; }
  }
  if (!ctrl) { return "the dial has no ×1 control setting"; }
  ctrl.click();
  var levels = w.querySelectorAll('.ks3-ba-level');
  for (i = 1; i < levels.length; i++) { w.querySelector('[data-ba-up]').click(); }
  // ⚖️⚖️ FLAT ALL THE WAY UP. Every level prints the SAME concentration, and
  // nothing anywhere on the bench is flagged as harmful. This is what proves
  // the mechanism is persistence and not toxicity — the claim rung 1 marks and
  // `#s-think` confronts. If the control ever stops being flat, the lesson has
  // lost the comparison it is built on.
  var ppms = w.querySelectorAll('[data-ba-ppm]'), first = ppms[0].textContent;
  for (i = 1; i < ppms.length; i++) {
    if (ppms[i].textContent !== first) {
      return "the ×1 control is not flat: " + first + " at the bottom and " +
        ppms[i].textContent + " at level " + (i + 1);
    }
  }
  if (w.querySelectorAll('.ks3-ba-level[data-harmful]').length) {
    return "the water-soluble control flagged a level as harmful";
  }
  var verdict = w.querySelector('.ks3-ba-verdict:not([hidden])');
  if (!verdict) { return "the control reached the top and no verdict landed"; }
  if (/[0-9]/.test(verdict.textContent.replace(/×1|x1/g, ''))) {
    return "the control's verdict quotes a figure; it is the one branch that " +
      "has no number to report: " + verdict.textContent;
  }
  return "";
})()
""",

    # b9-06, stage one. Takes a sample and proves the answer is still withheld.
    "b9-field-sampled": r"""
(function () {
  var sec = document.querySelector('[data-qbblock]');
  if (!sec) { return "no quadrat bench on the page"; }
  if (sec.getAttribute('data-stage-done') === '1') { return "the stop ticked on load"; }
  var w = sec.querySelector('[data-qb]');
  if (!w) { return "the practical shell rendered without the instrument"; }
  var count = sec.querySelector('[data-count]');
  if (count && count.textContent.indexOf('{') >= 0) {
    return "the head readout shipped an unfilled placeholder: " + count.textContent;
  }
  var side = parseInt(w.getAttribute('data-side'), 10);
  var cells = w.querySelectorAll('.ks3-qb-cell');
  if (cells.length !== side * side) {
    return "the field draws " + cells.length + " squares for a " + side + "×" + side + " site";
  }
  // ⚖️ AN UNSURVEYED FIELD SHOWS NOTHING. The counts are generated at page
  // load and none of them may be legible before a quadrat has been placed —
  // otherwise the estimate can be read off the grid and the reveal is spoiled.
  for (var i = 0; i < cells.length; i++) {
    if (cells[i].textContent.trim()) {
      return "square " + i + " shows its count before the field was surveyed";
    }
  }
  if (!w.querySelector('[data-qb-figures]').hasAttribute('hidden')) {
    return "the figures panel is open before a sample was taken";
  }
  // ⚠️ MRB-242 — AN AUTHOR `display` BEATS THE UA `[hidden]` RULE regardless of
  // specificity, and the element then ships visible with the attribute still on
  // it. Nine builds have paid for this. Probed rather than trusted: unset the
  // inline display, read what the STYLESHEET resolves to, put it back.
  var cascade = w.querySelectorAll(
    '.ks3-qb-figures[hidden], .ks3-qb-verdict[hidden]');
  for (var h = 0; h < cascade.length; h++) {
    var cel = cascade[h], cprev = cel.style.display;
    cel.style.display = '';
    var cshown = getComputedStyle(cel).display;
    cel.style.display = cprev;
    if (cshown !== 'none') {
      return "MRB-242: " + cel.className + " ships `hidden` but the stylesheet " +
        "gives it display:" + cshown + ", which beats the UA [hidden] rule";
    }
  }
  if (!w.querySelector('[data-qb-truth]').disabled) {
    return "the reveal is available before an estimate has been made";
  }
  w.querySelector('[data-qb-sample]').click();
  var marked = w.querySelectorAll('.ks3-qb-cell[data-in-sample]').length;
  var want = parseInt(w.getAttribute('data-count'), 10);
  if (marked !== want) {
    return "the sample counted " + marked + " squares against a dial of " + want;
  }
  var labelled = 0;
  for (var j = 0; j < cells.length; j++) {
    if (cells[j].textContent.trim()) { labelled += 1; }
  }
  if (labelled !== marked) {
    return labelled + " squares show a count and " + marked + " were sampled";
  }
  if (w.querySelector('[data-qb-figures]').hasAttribute('hidden')) {
    return "a sample was taken and the figures did not arrive";
  }
  if (w.querySelector('[data-qb-fig="real"]').textContent !==
      w.getAttribute('data-hidden-value')) {
    return "the real total was given away before the student asked for it";
  }
  if (w.querySelector('[data-qb-truth]').disabled) {
    return "a sample was taken and the reveal is still locked";
  }
  // ⚖️ THE RAIL TICKS ON THE REVEAL, NOT ON THE SAMPLE. Design's own
  // threshold: an estimate you have not checked is not the lesson.
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on the sample; it ticks on the reveal";
  }
  return "";
})()
""",

    # b9-06, stage two. Reveals the truth, and then proves the thing the whole
    # instrument exists for: more quadrats fixes chance and does nothing at all
    # for bias.
    "b9-field-revealed": r"""
(function () {
  var sec = document.querySelector('[data-qbblock]');
  if (!sec) { return "no quadrat bench on the page"; }
  var w = sec.querySelector('[data-qb]');
  if (!w) { return "the practical shell rendered without the instrument"; }
  w.querySelector('[data-qb-sample]').click();
  w.querySelector('[data-qb-truth]').click();
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "the real total was revealed and the stop did not tick";
  }
  var real = w.querySelector('[data-qb-fig="real"]').textContent;
  if (real === w.getAttribute('data-hidden-value') || !/[0-9]/.test(real)) {
    return "the reveal printed " + real;
  }
  var verdict = w.querySelector('[data-qb-verdict]:not([hidden])');
  if (!verdict) { return "the truth was shown and no verdict landed"; }
  if (verdict.textContent.indexOf('{') >= 0) {
    return "the verdict shipped an unfilled placeholder: " + verdict.textContent;
  }
  var cells = w.querySelectorAll('.ks3-qb-cell'), i, blank = 0;
  for (i = 0; i < cells.length; i++) { if (!cells[i].textContent.trim()) { blank += 1; } }
  if (blank) { return blank + " squares stayed hidden after the reveal"; }

  function err(method, n) {
    w.querySelector('[data-qb-method="' + method + '"]').click();
    w.querySelector('[data-qb-count="' + n + '"]').click();
    w.querySelector('[data-qb-sample]').click();
    w.querySelector('[data-qb-truth]').click();
    var m = /(\d+)%/.exec(w.querySelector('[data-qb-verdict]').textContent);
    return m ? parseInt(m[1], 10) : NaN;
  }
  function runs(method, n, k) {
    var out = [], j;
    for (j = 0; j < k; j++) { out.push(err(method, n)); }
    return out;
  }
  function mean(a) {
    var s = 0, j;
    for (j = 0; j < a.length; j++) { s += a[j]; }
    return s / a.length;
  }
  var counts = w.querySelectorAll('[data-qb-count]');
  var small = parseInt(counts[0].getAttribute('data-qb-count'), 10);
  var big = parseInt(counts[counts.length - 1].getAttribute('data-qb-count'), 10);

  // ⚖️⚖️ CHANCE SHRINKS WITH EFFORT AND BIAS DOES NOT. Twelve runs each way.
  // Random placement must get MEASURABLY better with the larger sample;
  // the flowery corner must not, and at its largest setting it exhausts its
  // own 25-cell pool and becomes DETERMINISTIC — the same wrong answer every
  // time. That separation is `NOS-04`'s whole confrontation, and it is the
  // property a "balanced" set of pools would silently delete.
  var rSmall = mean(runs('random', small, 12));
  var rBig = mean(runs('random', big, 12));
  if (!(rBig < rSmall)) {
    return "more random quadrats did not reduce the error: " + rSmall +
      "% at " + small + " and " + rBig + "% at " + big;
  }
  var cBig = runs('corner', big, 6);
  var spread = Math.max.apply(null, cBig) - Math.min.apply(null, cBig);
  if (spread !== 0) {
    return "the largest sample on the flowery corner still wobbles by " + spread +
      " points; it should exhaust its pool and be deterministic";
  }
  if (!(mean(cBig) > rBig)) {
    return "the flowery corner at " + big + " quadrats is no worse (" +
      mean(cBig) + "%) than random placement (" + rBig +
      "%) — the pools have been balanced and bias has stopped being bias";
  }
  var pBig = mean(runs('path', big, 6));
  if (!(pBig > rBig)) {
    return "the path edge at " + big + " quadrats is no worse (" + pBig +
      "%) than random placement — bias has no favourite direction, but it " +
      "must have a direction";
  }
  // ⚖️ AND SWITCHING THE DIAL PUTS THE ANSWER BACK. Re-sampling clears the
  // reveal; it does not untick the stop.
  w.querySelector('[data-qb-method="random"]').click();
  if (!w.querySelector('[data-qb-figures]').hasAttribute('hidden')) {
    return "switching method left the previous survey's figures on screen";
  }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "switching method unticked a stop the student had reached";
  }
  // Back to a REVEALED state for the driven rows.
  w.querySelector('[data-qb-sample]').click();
  w.querySelector('[data-qb-truth]').click();
  return "";
})()
""",

    # ═══ BEGIN B10 drives ═══
    # ⚖️ ONE CHARACTERISTIC PREDICTED AND PLOTTED, and the whole gate proved on
    # the way. b10-01 is Law 4 built into an instrument: the graph cannot be
    # reached until a shape has been committed to, the commitment cannot be
    # taken back once plotted, and there is no reset. Each of those is checked
    # here rather than described, and the driven rows below then measure the
    # verdict panel that arrives.
    "b10-plot-run": r"""
(function () {
  var sec = document.querySelector('[data-vpblock]');
  if (!sec) { return "no variation plotter on the page"; }
  if (sec.getAttribute('data-stage-done') === '1') { return "the stop ticked on load"; }
  var w = sec.querySelector('[data-vp]');
  if (!w) { return "the practical shell rendered without the instrument"; }
  var tabs = w.querySelectorAll('[data-vp-char]');
  if (tabs.length < 3) { return "the bench offers " + tabs.length + " characteristic(s)"; }
  // ⚠️ NARROWED, BY MUTATION. This used to test the whole section's innerHTML
  // for any `ks3-option`, and the predict buttons carry the class too — so
  // stripping it from every tab left the assertion green. Ask each tab.
  for (var c = 0; c < tabs.length; c++) {
    if (!/\bks3-option\b/.test(tabs[c].className)) {
      return "characteristic tab " + c + " is not a platform option: " + tabs[c].className;
    }
    if (tabs[c].getAttribute('aria-pressed') === null) {
      return "characteristic tab " + c + " carries no aria-pressed";
    }
  }
  var count = sec.querySelector('[data-count]');
  if (count && count.textContent.indexOf('{') >= 0) {
    return "the head readout shipped an unfilled placeholder: " + count.textContent;
  }
  // MRB-242: a stylesheet `display` on a `hidden` element beats the UA rule
  // and every hidden panel on this bench would be on screen at once.
  var cascade = w.querySelectorAll(
    '[data-vp-charpanel][hidden], [data-vp-graph][hidden], .ks3-vp-tag[hidden]');
  for (var h = 0; h < cascade.length; h++) {
    var el = cascade[h], prev = el.style.display;
    el.style.display = '';
    var shown = getComputedStyle(el).display;
    el.style.display = prev;
    if (shown !== 'none') {
      return "MRB-242: " + el.className + " ships `hidden` but the stylesheet " +
        "gives it display:" + shown + ", which beats the UA [hidden] rule";
    }
  }
  var open = w.querySelectorAll('[data-vp-charpanel]:not([hidden])');
  if (open.length !== 1) {
    return "the bench opens with " + open.length + " characteristics showing";
  }
  var panel = open[0];
  // ⚖️ LAW 4, IN THE SHIPPED BYTES. No prediction, no graph, and the control
  // that would produce one is disabled before any JS has run.
  var plot = w.querySelector('[data-vp-plot]');
  if (!plot.disabled) {
    return "the plot button is live before any shape has been predicted";
  }
  if (panel.querySelector('[data-vp-graph]:not([hidden])')) {
    return "the graph is on screen before the student committed to a shape";
  }
  if (!panel.querySelector('[data-vp-predict]:not([hidden])')) {
    return "the bench opens with no prediction to make";
  }
  var preds = panel.querySelectorAll('.ks3-vp-pred');
  if (preds.length !== 2) { return "the panel offers " + preds.length + " shape(s)"; }
  plot.click();
  if (panel.querySelector('[data-vp-graph]:not([hidden])')) {
    return "a click on the disabled plot button revealed the graph anyway";
  }
  preds[0].click();
  if (plot.disabled) { return "a shape was predicted and the plot button stayed dead"; }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on a prediction, before anything was plotted";
  }
  plot.click();
  var graph = panel.querySelector('[data-vp-graph]:not([hidden])');
  if (!graph) { return "the data was plotted and no graph arrived"; }
  if (panel.querySelector('[data-vp-predict]:not([hidden])')) {
    return "the prediction is spent and its buttons are still on screen";
  }
  if (!plot.disabled) { return "the graph is drawn and the plot button is still live"; }
  // ⚠️ AND THE BUTTON SAYS SO. `run_done_label` is authored, emitted and read;
  // without this the spent state is a dead label and the page reads
  // "Plot the data" over a graph that has already been plotted. Added by
  // mutation — swapping the runtime to `RUN` for ever passed everything else.
  var doneLabel = w.getAttribute('data-run-done-label');
  var runLabel = w.getAttribute('data-run-label');
  if (doneLabel === runLabel) {
    return "the bench authors one label for both states of the plot button";
  }
  if (plot.textContent.trim() !== doneLabel.trim()) {
    return "the plot button is spent and still reads " + JSON.stringify(plot.textContent);
  }
  // ⛔ ONE TAG, AND IT IS WORDS. The bench says whether the prediction held
  // (schema §0.6) and says it in one tone; it never marks the button.
  var tags = graph.querySelectorAll('.ks3-vp-tag:not([hidden])');
  if (tags.length !== 1) { return "the verdict shows " + tags.length + " tag(s)"; }
  var chosen = panel.querySelector('.ks3-vp-pred[aria-pressed="true"]');
  var want = chosen.getAttribute('data-vp-pred') ===
    graph.querySelector('.ks3-vp-chart').getAttribute('data-vp-type') ? 'right' : 'wrong';
  if (tags[0].getAttribute('data-vp-tag') !== want) {
    return "the prediction was " + want + " and the bench showed the other tag";
  }
  if (/is-correct|is-wrong|is-spent/.test(chosen.className)) {
    return "MRB-196 R10: the bench marked the prediction button — " + chosen.className;
  }
  // ⚖️ SHAPE AND CAUSE ARE TWO PARAGRAPHS AND THE RULE IS BETWEEN THEM.
  if (!graph.querySelector('.ks3-vp-shape') || !graph.querySelector('.ks3-vp-cause')) {
    return "the verdict panel merged the shape answer and the cause answer";
  }
  if (graph.querySelector('.ks3-vp-cause').textContent.indexOf(
        graph.querySelector('.ks3-vp-shape').textContent) >= 0) {
    return "the cause paragraph repeats the shape paragraph";
  }
  // ⚖️ AND THE PREDICTION CANNOT BE TAKEN BACK. There is no reset on this
  // bench: six characteristics, one prediction each.
  preds[1].click();
  if (panel.querySelector('.ks3-vp-pred[aria-pressed="true"]') !== chosen) {
    return "a plotted prediction was changed after the fact";
  }
  return "";
})()
""",

    # ⚖️⚖️ BOTH GAPS, MEASURED, ON THE SAME PAGE. This is the histogram /
    # bar-chart convention read off painted geometry rather than off the
    # stylesheet, and it is the one claim on this bench that a student takes
    # away as a rule. The column is `flex: 1 1 0`, so neither width is a fixed
    # number and both are a RELATION: a continuous bar is exactly its column
    # wide and its neighbour therefore touches it; a discontinuous bar is
    # exactly 6px narrower and its neighbour therefore does not. Schema §2
    # forbids an authored gap key precisely so that no record can ship
    # touching bars for blood group — this is what makes that stick.
    "b10-plot-both": r"""
(function () {
  var sec = document.querySelector('[data-vpblock]');
  if (!sec) { return "no variation plotter on the page"; }
  var w = sec.querySelector('[data-vp]');
  if (!w) { return "the practical shell rendered without the instrument"; }
  var tabs = document.querySelectorAll('[data-vp-char]');
  var seen = {}, apart = {};
  function plotCurrent() {
    var panel = w.querySelector('[data-vp-charpanel]:not([hidden])');
    var pred = panel.querySelector('.ks3-vp-pred');
    if (!pred) { return "a characteristic panel offers no shape to predict"; }
    pred.click();
    w.querySelector('[data-vp-plot]').click();
    var graph = panel.querySelector('[data-vp-graph]:not([hidden])');
    if (!graph) { return "a characteristic was plotted and no graph arrived"; }
    var chart = graph.querySelector('.ks3-vp-chart');
    var type = chart.getAttribute('data-vp-type');
    var cols = chart.querySelectorAll('.ks3-vp-col');
    if (cols.length < 2) { return type + " drew " + cols.length + " column(s)"; }
    var colW = cols[0].getBoundingClientRect().width;
    var barW = cols[0].querySelector('.ks3-vp-bar').getBoundingClientRect().width;
    var want = type === 'continuous' ? colW : colW - 6;
    if (Math.abs(barW - want) > 0.6) {
      return type + " bars are " + barW.toFixed(2) + "px in a " +
        colW.toFixed(2) + "px column; the derived gap wants " + want.toFixed(2) + "px";
    }
    // ⚖️⚖️ THE CLAIM THE WIDTH IS FOR: DO NEIGHBOURING BARS MEET, OR NOT.
    // Touching bars are what makes a histogram a histogram, and the axis
    // caption under this chart says so in words. Read off painted geometry,
    // because the stylesheet saying the right thing is not evidence that the
    // browser drew it.
    var a = cols[0].querySelector('.ks3-vp-bar').getBoundingClientRect();
    var b = cols[1].querySelector('.ks3-vp-bar').getBoundingClientRect();
    apart[type] = b.left - a.right;
    if (type === 'continuous' && apart[type] > 0.6) {
      return "continuous bars stand " + apart[type].toFixed(2) +
        "px apart, and the caption under them says they touch";
    }
    if (type === 'discontinuous' && apart[type] < 5.4) {
      return "discontinuous bars stand " + apart[type].toFixed(2) +
        "px apart; a bar chart's categories are separated";
    }
    // Every bar is on screen: the floor of 3% keeps a one-student bin visible.
    for (var q = 0; q < cols.length; q++) {
      if (cols[q].querySelector('.ks3-vp-bar').getBoundingClientRect().height < 1) {
        return type + " drew a bin with no bar at all";
      }
    }
    // ⊕ MRB-257 · audit 5.4 — AND THE HEIGHTS ARE THE RATIO THEY WERE
    // AUTHORED AS. This was the gap under the gap: the width rules above are
    // measured on painted geometry and the HEIGHTS were not measured at all,
    // so `.ks3-vp-bar` inheriting `flex-shrink: 1` inside a 146px column
    // whose labels took 42.4px drew every bar authored above 70.96% at
    // exactly 103.6px. Height's 81.25% / 100% / 75% all rendered 103.6 /
    // 103.6 / 103.6, under a verdict reading "a smooth hump... most people
    // are near the middle", over a flat-topped plateau. Eye colour drew a
    // true 2.0 ratio as 1.42.
    //
    // The claim is a RELATION, like the widths above: the tallest bar sets
    // the scale, and every other bar stands in the same proportion to it that
    // its authored percentage does. That cannot be a `props` row — it is two
    // measurements — and it is what a student reads the chart FOR.
    var pcts = [], pxs = [], topPct = 0, topPx = 0;
    for (var h = 0; h < cols.length; h++) {
      var barEl = cols[h].querySelector('.ks3-vp-bar');
      var pc = parseFloat(barEl.style.height);
      if (!(pc > 0)) {
        return type + " bin " + h + " carries no authored height (style.height "
          + JSON.stringify(barEl.style.height) + "), so the ratio the chart "
          + "claims cannot be checked against anything";
      }
      var px = barEl.getBoundingClientRect().height;
      pcts.push(pc); pxs.push(px);
      if (pc > topPct) { topPct = pc; topPx = px; }
    }
    for (var h2 = 0; h2 < cols.length; h2++) {
      var want = (pcts[h2] / topPct) * topPx;
      if (Math.abs(pxs[h2] - want) > 1.5) {
        return type + " bin " + h2 + " is authored at " + pcts[h2] +
          "% of a " + topPct + "% tallest bar and is DRAWN at " +
          pxs[h2].toFixed(1) + "px against the tallest bar's " +
          topPx.toFixed(1) + "px — it should be " + want.toFixed(1) +
          "px. The chart is not showing the distribution it was given.";
      }
    }
    seen[type] = true;
    return "";
  }
  // ⚖️⚖️ DESIGN'S THRESHOLD, COUNTED IN, ONE AT A TIME. `s-bench` and the
  // `s-two` band stop that MIRRORS it both tick on this number (MRB-249), so
  // an off-by-one here moves two rail stops. Asserted in both directions:
  // nothing ticks before the threshold, and it ticks at it. Added by mutation
  // — reading the threshold as 1 passed a loop that plotted everything.
  var NEED = parseInt(w.getAttribute('data-threshold'), 10);
  if (!(NEED >= 2)) { return "the bench declares a threshold of " + NEED; }
  for (var i = 0; i < tabs.length; i++) {
    tabs[i].click();
    var err = plotCurrent();
    if (err) { return err; }
    var ticked = sec.getAttribute('data-stage-done') === '1';
    if (i + 1 < NEED && ticked) {
      return "the stop ticked after " + (i + 1) + " plotted, and the threshold is " + NEED;
    }
    if (i + 1 >= NEED && !ticked) {
      return "the stop had not ticked after " + (i + 1) +
        " plotted, and the threshold is " + NEED;
    }
    if (i + 1 >= NEED && seen.continuous && seen.discontinuous) { break; }
  }
  if (!seen.continuous || !seen.discontinuous) {
    return "the bench never drew both kinds of data: " + JSON.stringify(seen);
  }
  // ⚖️⚖️ SIX PIXELS, EXACTLY, AND IT IS THE WHOLE CONVENTION. Not a style
  // preference and not a number a payload may set: schema §2 forbids a `gap`
  // key so that no record can ship blood group drawn as a histogram.
  if (Math.abs((apart.discontinuous - apart.continuous) - 6) > 0.6) {
    return "discontinuous bars stand " + apart.discontinuous.toFixed(2) +
      "px apart and continuous ones " + apart.continuous.toFixed(2) +
      "px; the derived gap is 6px and this is " +
      (apart.discontinuous - apart.continuous).toFixed(2);
  }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "the bench reached its threshold and the stop did not tick";
  }
  // ⚠️ MONOTONIC. Switching back to a characteristic already plotted must not
  // untick a stop the student reached — MRB-208, and the `s-two` band stop
  // mirrors this one, so it would untick two.
  tabs[0].click();
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "switching characteristic unticked a stop already reached";
  }
  return "";
})()
""",

    # ⚖️ ALL SIX LEVELS, ONE PRESS AT A TIME. Design's own `isDone()` is
    # `s.shown >= LEVELS.length` and the `s-model` band stop MIRRORS it
    # (MRB-249), so this threshold is read by two rail entries. The whole
    # ladder must be drawn from the first paint — the scale column is the
    # lesson's argument and it cannot be read one row at a time — while only
    # the `body` arrives on a press.
    "b10-zoom-bottomed": r"""
(function () {
  var sec = document.querySelector('[data-zbblock]');
  if (!sec) { return "no zoom bench on the page"; }
  if (sec.getAttribute('data-stage-done') === '1') { return "the stop ticked on load"; }
  var w = sec.querySelector('[data-zb]');
  if (!w) { return "the practical shell rendered without the instrument"; }
  var levels = w.querySelectorAll('.ks3-zb-level');
  var total = parseInt(w.getAttribute('data-total'), 10);
  if (levels.length !== total || !(total >= 3)) {
    return "the bench declares " + total + " levels and draws " + levels.length;
  }
  var count = sec.querySelector('[data-count]');
  if (count && count.textContent.indexOf('{') >= 0) {
    return "the head readout shipped an unfilled placeholder: " + count.textContent;
  }
  // MRB-242: a stylesheet `display` beats the UA [hidden] rule.
  var cascade = w.querySelectorAll('.ks3-zb-body[hidden], .ks3-zb-close[hidden], [data-zb-answer][hidden]');
  for (var h = 0; h < cascade.length; h++) {
    var el = cascade[h], prev = el.style.display;
    el.style.display = '';
    var d = getComputedStyle(el).display;
    el.style.display = prev;
    if (shownDisplay(d)) {
      return "MRB-242: " + el.className + " ships `hidden` but the stylesheet " +
        "gives it display:" + d + ", which beats the UA [hidden] rule";
    }
  }
  function shownDisplay(d) { return d !== 'none'; }
  // ⚖️⚖️ EVERY LEVEL IS DRAWN FROM THE START. The scale column is the argument
  // and it has to be readable as a column before the journey begins.
  for (var i = 0; i < levels.length; i++) {
    var r = levels[i].getBoundingClientRect();
    if (r.width < 1 || r.height < 1) {
      return "level " + (i + 1) + " is not drawn until it is reached";
    }
    var sc = levels[i].querySelector('.ks3-zb-scale');
    if (!sc || !sc.textContent.trim()) {
      return "level " + (i + 1) + " prints no scale, and the scale column is the argument";
    }
    if (sc.getBoundingClientRect().width < 1) {
      return "level " + (i + 1) + "'s scale figure is not drawn";
    }
  }
  if (w.querySelectorAll('.ks3-zb-body:not([hidden])').length !== 1) {
    return "the bench opens with more than the first level's body revealed";
  }
  if (w.querySelector('.ks3-zb-close:not([hidden])')) {
    return "the bottom-out paragraph landed before the bench reached the bottom";
  }
  if (w.querySelectorAll('.ks3-zb-level[data-here]').length !== 1) {
    return "the bench opens with no single level marked as where you are";
  }
  var inBtn = w.querySelector('[data-zb-in]');
  var IN = w.getAttribute('data-in-label'), DONE = w.getAttribute('data-in-done-label');
  if (IN === DONE) { return "the bench authors one label for both states of the zoom button"; }
  if (inBtn.textContent.trim() !== IN.trim()) {
    return "the zoom button opens reading " + JSON.stringify(inBtn.textContent);
  }
  for (var k = 1; k < total; k++) {
    if (inBtn.disabled) { return "the zoom button locked at level " + k; }
    inBtn.click();
    var open = w.querySelectorAll('.ks3-zb-body:not([hidden])').length;
    if (open !== k + 1) {
      return "press " + k + " revealed " + open + " level(s); each press reveals one";
    }
    if (w.querySelectorAll('.ks3-zb-level[data-here]').length !== 1) {
      return "press " + k + " left " + w.querySelectorAll('.ks3-zb-level[data-here]').length +
        " levels marked as where you are";
    }
    if (k < total - 1) {
      if (w.querySelector('.ks3-zb-close:not([hidden])')) {
        return "the bottom-out paragraph landed at level " + (k + 1) + " of " + total;
      }
      if (sec.getAttribute('data-stage-done') === '1') {
        return "the stop ticked at level " + (k + 1) + " of " + total;
      }
    }
  }
  if (!w.querySelector('.ks3-zb-close:not([hidden])')) {
    return "the bench reached the bottom and no closing paragraph arrived";
  }
  if (!inBtn.disabled) { return "the bench is at the bottom and the zoom button is still live"; }
  if (inBtn.textContent.trim() !== DONE.trim()) {
    return "the zoom button is spent and still reads " + JSON.stringify(inBtn.textContent);
  }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "all six levels are open and the stop did not tick";
  }
  // ⚖️ THE SAY-IT-BACK PANEL GATES NOTHING AND MARKS NOTHING. One answer is
  // shown at a time, the pressed tab says which question is being looked at,
  // and no tab carries a verdict class (MRB-196 R10).
  var qtabs = w.querySelectorAll('.ks3-zb-qtab');
  if (qtabs.length < 2) { return "the say-it-back panel offers " + qtabs.length + " question(s)"; }
  var pressed = w.querySelectorAll('.ks3-zb-qtab[aria-pressed="true"]');
  if (pressed.length !== 1) {
    return "the say-it-back panel opens with " + pressed.length + " questions chosen";
  }
  // ⚠️ `opens_on` IS NOT THE FIRST QUESTION, and that is the whole reason the
  // key exists (schema §3.2). If the panel ever opens on tab 0 the key has
  // stopped being read and the opening question is list order, not teaching.
  if (pressed[0] === qtabs[0]) {
    return "the say-it-back panel opened on the FIRST question; `opens_on` names another";
  }
  for (var q = 0; q < qtabs.length; q++) {
    qtabs[q].click();
    var vis = w.querySelectorAll('[data-zb-answer]:not([hidden])');
    if (vis.length !== 1) { return "question " + q + " shows " + vis.length + " answer(s)"; }
    if (vis[0].getAttribute('data-zb-answer') !== qtabs[q].getAttribute('data-zb-q')) {
      return "question " + q + " shows another question's answer";
    }
    if (/is-correct|is-wrong|is-spent/.test(qtabs[q].className)) {
      return "MRB-196 R10: the say-it-back panel marked a question — " + qtabs[q].className;
    }
    if (sec.getAttribute('data-stage-done') !== '1') {
      return "reading an answer unticked a stop already reached";
    }
  }
  // ⚠️ `Back out` IS A VIEW RESET, NOT A RECORD RESET. MRB-208: what a student
  // found out cannot be un-found — and two stops read this marker.
  var outBtn = w.querySelector('[data-zb-out]');
  if (outBtn) {
    outBtn.click();
    if (sec.getAttribute('data-stage-done') !== '1') {
      return "backing out unticked a stop already reached";
    }
    if (w.querySelectorAll('.ks3-zb-body:not([hidden])').length !== 1) {
      return "backing out did not return the bench to the first level";
    }
    if (w.querySelector('.ks3-zb-close:not([hidden])')) {
      return "the bottom-out paragraph survived a back-out";
    }
  }
  // Leave the bench BOTTOMED for the driven rows.
  for (var z = 1; z < total; z++) { w.querySelector('[data-zb-in]').click(); }
  return "";
})()
""",

    # ⚖️⚖️ TWELVE MODELS, FOUR TESTS, AND EXACTLY ONE SURVIVOR — walked in a
    # browser rather than trusted from the matrix in schema §4.2. The bench
    # must open on the unique 0-of-4 row (Pauling's model), every dial press
    # must re-evaluate all four cards live with no run button anywhere, and
    # only `correct` may reach 4 of 4.
    "b10-model-solved": r"""
(function () {
  var sec = document.querySelector('[data-dhblock]');
  if (!sec) { return "no model builder on the page"; }
  if (sec.getAttribute('data-stage-done') === '1') { return "the stop ticked on load"; }
  var w = sec.querySelector('[data-dh]');
  if (!w) { return "the practical shell rendered without the instrument"; }
  var cards = w.querySelectorAll('[data-dh-card]');
  var total = parseInt(w.getAttribute('data-total'), 10);
  if (cards.length !== total || !(total >= 2)) {
    return "the bench declares " + total + " tests and draws " + cards.length;
  }
  // ⛔ NO RUN BUTTON AND NO RESET BUTTON (schema §4.3). The cards re-evaluate
  // live; a control here would be one Design did not draw.
  if (w.querySelector('.ks3-reveal-btn')) {
    return "the bench grew a run or reset control; the cards re-evaluate live";
  }
  var count = sec.querySelector('[data-count]');
  if (count && count.textContent.indexOf('{') >= 0) {
    return "the head readout shipped an unfilled placeholder: " + count.textContent;
  }
  // MRB-242: a stylesheet `display` on a `hidden` element beats the UA rule,
  // and every elimination line and both verdict tags on every card would be on
  // screen at once — a bench saying `consistent` and `rules this model out`
  // about the same evidence in the same row.
  //
  // ⚠️ RUN WHEN SOMETHING IS ACTUALLY HIDDEN. The bench OPENS with every card
  // failing, so at rest there is not one hidden `why` to sweep and the check
  // passes over an empty list. Called from inside the walk below, the first
  // time a model passes anything. Added by mutation, and the first cut of it
  // was the empty sweep.
  function cascade() {
    var els = w.querySelectorAll('.ks3-dh-why[hidden], .ks3-dh-tag[hidden]');
    if (!els.length) { return "nothing was hidden to check"; }
    for (var h = 0; h < els.length; h++) {
      var el = els[h], prev = el.style.display;
      el.style.display = '';
      var shown = getComputedStyle(el).display;
      el.style.display = prev;
      if (shown !== 'none') {
        return "MRB-242: " + el.className + " ships `hidden` but the stylesheet " +
          "gives it display:" + shown + ", which beats the UA [hidden] rule";
      }
    }
    return "";
  }
  var swept = false;
  var line = w.querySelector('[data-dh-modelline]');
  if (!line || !line.textContent.trim()) { return "the bench prints no model line"; }
  var tag = w.querySelector('[data-dh-verdicttag]');
  if (tag.textContent.indexOf('{') >= 0) {
    return "the verdict tag shipped an unfilled placeholder: " + tag.textContent;
  }
  // ⚖️⚖️ THE OPENING STATE IS THE PRESET AND IT IS THE UNIQUE 0-OF-N ROW.
  // Every card red, so every dial the student touches can only improve it.
  if (w.querySelectorAll('[data-dh-card][data-pass]').length !== 0) {
    return "the bench opens with " + w.querySelectorAll('[data-dh-card][data-pass]').length +
      " card(s) already passing; the preset is the unique row that fails everything";
  }
  if (w.querySelectorAll('.ks3-dh-why:not([hidden])').length !== total) {
    return "the bench opens with " + w.querySelectorAll('.ks3-dh-why:not([hidden])').length +
      " elimination line(s) showing, and " + total + " cards are failing";
  }
  var CORRECT = JSON.parse(w.getAttribute('data-target') || '{}');
  var opts = w.querySelectorAll('.ks3-dh-opt');
  // ⛔ A DIAL IS NEVER MARKED (MRB-196 R10). The bench opens on a WRONG model
  // with all its dials pressed; a verdict class here would open by telling the
  // student they were right.
  var d;
  for (d = 0; d < opts.length; d++) {
    if (/is-correct|is-wrong|is-spent/.test(opts[d].className)) {
      return "MRB-196 R10: a dial button carries a verdict class — " + opts[d].className;
    }
  }
  // Walk EVERY combination of every dial and score it against the cards, the
  // way a student would. Exactly one may reach four of four.
  var dials = {}, order = [];
  for (d = 0; d < opts.length; d++) {
    var id = opts[d].getAttribute('data-dh-dial');
    if (!dials[id]) { dials[id] = []; order.push(id); }
    dials[id].push(opts[d]);
  }
  function press(btn) { btn.click(); }
  function passing() { return w.querySelectorAll('[data-dh-card][data-pass]').length; }
  var combos = [[]], i, j, k, next;
  for (i = 0; i < order.length; i++) {
    next = [];
    for (j = 0; j < combos.length; j++) {
      for (k = 0; k < dials[order[i]].length; k++) {
        next.push(combos[j].concat([dials[order[i]][k]]));
      }
    }
    combos = next;
  }
  var perfect = 0, zero = 0, solvedAt = -1;
  for (i = 0; i < combos.length; i++) {
    for (j = 0; j < combos[i].length; j++) { press(combos[i][j]); }
    var n = passing();
    if (w.querySelectorAll('.ks3-dh-why:not([hidden])').length !== total - n) {
      return "a model passing " + n + " of " + total +
        " showed " + w.querySelectorAll('.ks3-dh-why:not([hidden])').length + " elimination line(s)";
    }
    if (n > 0 && !swept) {
      var cerr = cascade();
      if (cerr && cerr !== "nothing was hidden to check") { return cerr; }
      if (!cerr) { swept = true; }
    }
    if (n === total) {
      perfect += 1;
      solvedAt = i;
      var built = {}, kk;
      for (j = 0; j < combos[i].length; j++) {
        built[combos[i][j].getAttribute('data-dh-dial')] =
          combos[i][j].getAttribute('data-dh-opt');
      }
      for (kk in CORRECT) {
        if (built[kk] !== CORRECT[kk]) {
          return "a model that is not `correct` passed every test: " + JSON.stringify(built);
        }
      }
      if (sec.getAttribute('data-stage-done') !== '1') {
        return "every test passed and the stop did not tick";
      }
    }
    if (n === 0) { zero += 1; }
  }
  if (perfect !== 1) {
    return "of " + combos.length + " models, " + perfect +
      " pass every test; the lesson's claim is that exactly one does";
  }
  if (zero !== 1) {
    return "of " + combos.length + " models, " + zero +
      " fail every test; the opening preset is meant to be the unique one";
  }
  if (!swept) { return "no model on this bench ever hid an elimination line"; }
  // ⚠️ `solved` IS STICKY. Break the model on purpose and the stop stays —
  // MRB-208, and the `s-who` band stop mirrors this marker, so an unticking
  // predicate would move two.
  dials[order[0]][0].click();
  dials[order[0]][dials[order[0]].length - 1].click();
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "breaking the model after solving it unticked the stop";
  }
  // Leave the bench SOLVED for the driven rows.
  for (j = 0; j < combos[solvedAt].length; j++) { press(combos[solvedAt][j]); }
  if (passing() !== total) { return "the bench could not be returned to the solved model"; }
  return "";
})()
""",

    # ⚖️⚖️ REAL, UNSEEDED RANDOMNESS — so every assertion below is an INVARIANT
    # that holds across runs, never a pinned sequence. Schema §5.1: no student
    # sees the same cross twice, and a gate that needed them to would be a gate
    # arguing for a seed.
    "b10-cross-grown": r"""
(function () {
  var sec = document.querySelector('[data-pcblock]');
  if (!sec) { return "no pea cross on the page"; }
  if (sec.getAttribute('data-stage-done') === '1') { return "the stop ticked on load"; }
  var w = sec.querySelector('[data-pc]');
  if (!w) { return "the practical shell rendered without the instrument"; }
  var one = w.querySelector('[data-pc-one]'), many = w.querySelector('[data-pc-many]');
  var clear = w.querySelector('[data-pc-clear]');
  if (!one || !many) { return "the bench offers no way to grow a seed"; }
  var rows = w.querySelectorAll('[data-pc-row]');
  if (rows.length !== 2) { return "the plot tallies " + rows.length + " outcome(s)"; }
  var MANY = parseInt(w.getAttribute('data-many-n'), 10);
  if (!(MANY >= 20)) { return "the big button grows " + MANY + " seeds"; }
  // The plot opens empty: no tally, no seed card, and a note that already fits
  // the opening cross.
  if (w.querySelector('[data-pc-tally]:not([hidden])')) {
    return "the plot opens with a tally on it and no seeds grown";
  }
  if (w.querySelector('[data-pc-last]:not([hidden])')) {
    return "the plot opens with a most-recent seed and none has been grown";
  }
  if (w.querySelectorAll('[data-pc-note]:not([hidden])').length !== 1) {
    return "the plot opens with " +
      w.querySelectorAll('[data-pc-note]:not([hidden])').length + " notes showing";
  }
  var openingNote = w.querySelector('[data-pc-note]:not([hidden])').getAttribute('data-pc-note');
  var cross = w.querySelector('[data-pc-crossline]').textContent;
  if (cross.indexOf('{') >= 0) { return "the cross line shipped a placeholder: " + cross; }
  function total() {
    var t = 0, i, v;
    for (i = 0; i < rows.length; i++) {
      v = rows[i].querySelector('[data-pc-value]').textContent;
      t += parseInt(v, 10) || 0;
    }
    return t;
  }
  // ── one seed: the "chance decides each one" story ──
  one.click();
  if (total() !== 1) { return "growing one seed tallied " + total(); }
  var last = w.querySelector('[data-pc-last]:not([hidden])');
  if (!last) { return "growing one seed produced no most-recent-seed card"; }
  var line = w.querySelector('[data-pc-lastline]').textContent;
  if (line.indexOf('{') >= 0) { return "the seed line shipped a placeholder: " + line; }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked after one seed; the threshold is twenty";
  }
  // ── a hundred seeds: the "only totals show the pattern" story, and the two
  // are never on screen together ──
  many.click();
  if (total() !== 1 + MANY) { return "growing " + MANY + " more tallied " + total(); }
  if (w.querySelector('[data-pc-last]:not([hidden])')) {
    return "growing a hundred left the single-seed card on screen; the two stories are separate";
  }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "the plot passed twenty seeds and the stop did not tick";
  }
  // Both bars are drawn and the bars sum to the seeds. Pp × Pp cannot be all
  // one colour over a hundred and one seeds in any run this side of the heat
  // death of the universe, so this is an invariant and not a pinned outcome.
  var i, n, sum = 0;
  for (i = 0; i < rows.length; i++) {
    n = parseInt(rows[i].querySelector('[data-pc-value]').textContent, 10);
    sum += n;
    if (rows[i].querySelector('[data-pc-bar]').getBoundingClientRect().width < 0 ) {
      return "a tally bar has no width at all";
    }
  }
  if (sum !== total()) { return "the tally rows do not sum to the seeds grown"; }
  var ratio = w.querySelector('[data-pc-ratio]').textContent;
  if (!ratio.trim()) { return "a hundred seeds and the plot reports no ratio at all"; }
  if (ratio.indexOf('{') >= 0) { return "the ratio line shipped a placeholder: " + ratio; }
  // ⚖️⚖️ DOMINANT-FIRST, ALWAYS — AND DRIVEN DETERMINISTICALLY, WITHOUT A
  // SEED. `pP` is two spellings of one genotype and a student reasonably reads
  // them as two different things. Growing seeds and hoping for the p-then-P
  // case is a one-in-four assertion that passes three runs in four whatever
  // the code does — found by mutation, which slipped through exactly that way.
  // `pp x PP` forces it: parent 1 can only give p and parent 2 can only give
  // P, so EVERY seed is the case being tested. Real randomness, no seed, and a
  // certain outcome, because the cross was chosen rather than the dice.
  var pureRec = null, pureDom = null, gi;
  var allGeno = w.querySelectorAll('.ks3-pc-geno');
  var GEN = JSON.parse(w.getAttribute('data-genotypes') || '{}');
  var D = w.getAttribute('data-dominant'), R = w.getAttribute('data-recessive');
  var p1 = allGeno[0].getAttribute('data-pc-parent'), p2 = null;
  for (gi = 0; gi < allGeno.length; gi++) {
    if (allGeno[gi].getAttribute('data-pc-parent') !== p1) {
      p2 = allGeno[gi].getAttribute('data-pc-parent'); break;
    }
  }
  for (gi = 0; gi < allGeno.length; gi++) {
    var gid = allGeno[gi].getAttribute('data-pc-geno'), al = GEN[gid] || [];
    var isRec = al.length === 2 && al[0] === R && al[1] === R;
    var isDom = al.length === 2 && al[0] === D && al[1] === D;
    if (isRec && allGeno[gi].getAttribute('data-pc-parent') === p1) { pureRec = allGeno[gi]; }
    if (isDom && allGeno[gi].getAttribute('data-pc-parent') === p2) { pureDom = allGeno[gi]; }
  }
  if (!pureRec || !pureDom) {
    return "the bench cannot be set to a cross that forces the p-then-P seed";
  }
  pureRec.click();
  pureDom.click();
  w.querySelector('[data-pc-one]').click();
  var forced = w.querySelector('[data-pc-lastline]').textContent;
  if (forced.indexOf(R + D) >= 0) {
    return "the seed line printed " + R + D + " rather than " + D + R +
      "; the genotype is normalised dominant-first: " + forced;
  }
  if (forced.indexOf('so it is ' + D + R) < 0) {
    return "a " + R + R + " x " + D + D + " cross did not print " + D + R + ": " + forced;
  }
  // ⚠️ CHANGING A PARENT CLEARS THE PLOT. Counts carried across two different
  // crosses describe neither of them.
  var genos = w.querySelectorAll('.ks3-pc-geno');
  var firstParent = genos[0].getAttribute('data-pc-parent'), other = null;
  for (i = 0; i < genos.length; i++) {
    if (genos[i].getAttribute('data-pc-parent') === firstParent &&
        genos[i].getAttribute('aria-pressed') === 'false') { other = genos[i]; break; }
  }
  if (!other) { return "the first parent offers no other genotype"; }
  other.click();
  if (total() !== 0) {
    return "changing a parent left " + total() + " seeds on the plot from the previous cross";
  }
  if (w.querySelector('[data-pc-last]:not([hidden])')) {
    return "changing a parent left the previous cross's seed card on screen";
  }
  if (w.querySelector('[data-pc-tally]:not([hidden])')) {
    return "changing a parent left the previous cross's tally on screen";
  }
  var note2 = w.querySelector('[data-pc-note]:not([hidden])');
  if (!note2) { return "changing a parent left the plot with no note"; }
  if (note2.getAttribute('data-pc-note') === openingNote &&
      openingNote === 'both_carriers') {
    return "changing a parent off Pp x Pp left the both-carriers note in place";
  }
  // ⚠️ AND MONOTONIC: clearing the plot is a view reset, not a record reset.
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "changing a parent unticked a stop already reached";
  }
  if (clear) {
    clear.click();
    if (sec.getAttribute('data-stage-done') !== '1') {
      return "clearing the plot unticked a stop already reached";
    }
  }
  // Leave the bench with ONE seed on the opening cross, for the driven rows.
  for (i = 0; i < genos.length; i++) {
    if (genos[i].getAttribute('data-pc-parent') === firstParent) { genos[i].click(); break; }
  }
  w.querySelector('[data-pc-one]').click();
  return "";
})()
""",

    # ⚖️ SEVEN CASES, THREE VERDICTS, AND THE THIRD IS THE INSTRUMENT. The
    # bench is commit-then-reveal per case; the drive proves the gate, the
    # freeze, the threshold and — the thing that would be easiest to lose —
    # that "the test does not settle it" is somebody's correct answer.
    "b10-species-checked": r"""
(function () {
  var sec = document.querySelector('[data-scblock]');
  if (!sec) { return "no species bench on the page"; }
  if (sec.getAttribute('data-stage-done') === '1') { return "the stop ticked on load"; }
  var w = sec.querySelector('[data-sc]');
  if (!w) { return "the practical shell rendered without the instrument"; }
  var tabs = w.querySelectorAll('[data-sc-case]');
  var panels = w.querySelectorAll('[data-sc-panel]');
  var check = w.querySelector('[data-sc-check]');
  var NEED = parseInt(w.getAttribute('data-threshold'), 10);
  if (tabs.length !== panels.length || !(tabs.length >= NEED)) {
    return "the bench draws " + tabs.length + " tabs, " + panels.length +
      " panels and needs " + NEED;
  }
  if (w.querySelectorAll('[data-sc-panel]:not([hidden])').length !== 1) {
    return "the bench opens with more than one case showing";
  }
  // Law 4: no outcome before a commitment, and the control says so.
  if (!check.disabled) { return "the check button is live before any verdict is chosen"; }
  if (w.querySelector('[data-sc-out]:not([hidden])')) {
    return "an outcome is on screen before the student committed";
  }
  var count = sec.querySelector('[data-count]');
  if (count && count.textContent.indexOf('{') >= 0) {
    return "the head readout shipped an unfilled placeholder: " + count.textContent;
  }
  // ⚖️⚖️ THE THIRD VERDICT IS SOMEBODY'S ANSWER. A bench that offers "the test
  // does not settle it" and never lands on it teaches that the honest answer
  // is the box you do not tick.
  var third = null, answers = {}, i, j;
  var v0 = panels[0].querySelectorAll('.ks3-sc-verdict');
  if (v0.length !== 3) { return "the bench offers " + v0.length + " verdicts, and there are three"; }
  third = v0[2].getAttribute('data-sc-verdict');
  for (i = 0; i < panels.length; i++) {
    answers[panels[i].getAttribute('data-sc-answer')] = true;
    var letters = panels[i].querySelectorAll('.ks3-sc-letter');
    for (j = 0; j < letters.length; j++) {
      if (letters[j].textContent.trim() !== String.fromCharCode(65 + j)) {
        return "verdict " + j + " is lettered " + letters[j].textContent +
          "; the letters are derived from position";
      }
    }
  }
  if (!answers[third]) {
    return "no case answers the third verdict, which is the instrument of this lesson";
  }
  var tally = w.querySelector('[data-sc-tally]');
  var opened = 0;
  for (i = 0; i < tabs.length; i++) {
    tabs[i].click();
    var panel = w.querySelector('[data-sc-panel]:not([hidden])');
    if (panel.getAttribute('data-sc-panel') !== tabs[i].getAttribute('data-sc-case')) {
      return "tab " + i + " opened another case";
    }
    if (check.disabled === false && !panel.hasAttribute('data-sc-opened')) {
      return "case " + i + " arrived with the check button already live";
    }
    var opts = panel.querySelectorAll('.ks3-sc-verdict');
    // Answer the first three RIGHT and the rest WRONG, so both tags are
    // exercised in one document.
    var want = i < 3 ? panel.getAttribute('data-sc-answer') : null;
    var chosen = null;
    for (j = 0; j < opts.length; j++) {
      var id = opts[j].getAttribute('data-sc-verdict');
      if (want ? id === want : id !== panel.getAttribute('data-sc-answer')) {
        chosen = opts[j]; break;
      }
    }
    if (!chosen) { return "case " + i + " offers no verdict to choose"; }
    chosen.click();
    if (check.disabled) { return "case " + i + " had a verdict chosen and the check stayed dead"; }
    check.click();
    opened += 1;
    var out = panel.querySelector('[data-sc-out]:not([hidden])');
    if (!out) { return "case " + i + " was checked and no outcome arrived"; }
    var tags = out.querySelectorAll('.ks3-sc-tag:not([hidden])');
    if (tags.length !== 1) { return "case " + i + " showed " + tags.length + " outcome tag(s)"; }
    var wantTag = chosen.getAttribute('data-sc-verdict') ===
      panel.getAttribute('data-sc-answer') ? 'right' : 'wrong';
    if (tags[0].getAttribute('data-sc-tag') !== wantTag) {
      return "case " + i + " was answered " + wantTag + " and the bench showed the other tag";
    }
    // ⛔ AND THE BUTTON IS NEVER MARKED (MRB-196 R10).
    for (j = 0; j < opts.length; j++) {
      if (/is-correct|is-wrong|is-spent/.test(opts[j].className)) {
        return "MRB-196 R10: the bench marked a verdict button — " + opts[j].className;
      }
    }
    if (!panel.hasAttribute('data-sc-opened')) {
      return "case " + i + " was checked and the panel did not record it as settled";
    }
    // The commitment is FROZEN once checked.
    for (j = 0; j < opts.length; j++) { if (opts[j] !== chosen) { opts[j].click(); } }
    if (panel.querySelector('.ks3-sc-verdict[aria-pressed="true"]') !== chosen) {
      return "case " + i + " was settled and its verdict could still be changed";
    }
    if (!check.disabled) { return "case " + i + " was settled and the check button is still live"; }
    if (tally && tally.textContent.indexOf('{') >= 0) {
      return "the tally shipped an unfilled placeholder: " + tally.textContent;
    }
    var ticked = sec.getAttribute('data-stage-done') === '1';
    if (opened < NEED && ticked) {
      return "the stop ticked after " + opened + " settled, and the threshold is " + NEED;
    }
    if (opened >= NEED && !ticked) {
      return "the stop had not ticked after " + opened + " settled, and the threshold is " + NEED;
    }
  }
  if (tally && !/\S/.test(tally.textContent)) { return "the tally emptied at the end"; }
  // ⚠️ Revisiting a settled case does not untick anything (MRB-208), and the
  // `s-test` band stop mirrors this marker.
  tabs[0].click();
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "revisiting a settled case unticked a stop already reached";
  }
  return "";
})()
""",
    # ═══ END B10 drives ═══
    # ═══ BEGIN B11 drives ═══
    # ⚖️ THREE WORLDS SWITCHED THROUGH, AND THE BENCH ENDS ON THE TIE. b11-01
    # is a switcher with no run button and no reset, so what there is to prove
    # is: nothing ticks on load, the count is the number of worlds SEEN and
    # never shrinks, the stage flips on Design's own `n >= 3`, and — the one
    # place this port departs from her renderer — the `disease` column, whose
    # maximum is 45 on four of five mice, marks NOTHING. Her `isBest` is
    # `c === Math.max(…)`, so her page paints four green "best here" winners
    # under a verdict reading "None of the visible variations helps."
    #
    # ⚠️ THE TIED PANEL IS LEFT OPEN DELIBERATELY. Two driven rows above read
    # every bar and every figure in the open panel and demand the muted tone —
    # which is an assertion about ALL FIVE rows at once, and it is the shape
    # the defect had.
    "b11-conditions-tried": r"""
(function () {
  var sec = document.querySelector('[data-abblock]');
  if (!sec) { return "no advantage bench on the page"; }
  if (sec.getAttribute('data-stage-done') === '1') { return "the stop ticked on load"; }
  var w = sec.querySelector('[data-ab]');
  if (!w) { return "the practical shell rendered without the instrument"; }
  var need = Number(w.getAttribute('data-threshold'));
  if (!need) { return "the bench declares no completion threshold"; }
  var tabs = w.querySelectorAll('[data-ab-env]');
  if (tabs.length < need) {
    return "the bench offers " + tabs.length + " condition(s) and needs " + need;
  }
  for (var c = 0; c < tabs.length; c++) {
    if (!/\bks3-option\b/.test(tabs[c].className)) {
      return "condition tab " + c + " is not a platform option: " + tabs[c].className;
    }
    if (tabs[c].getAttribute('aria-pressed') === null) {
      return "condition tab " + c + " carries no aria-pressed";
    }
  }
  var count = sec.querySelector('[data-count]');
  if (!count) { return "the bench ships no head readout"; }
  if (count.textContent.indexOf('{') >= 0) {
    return "the head readout shipped an unfilled placeholder: " + count.textContent;
  }
  // ⚠️ THE RESTING COUNT IS ONE, NOT ZERO. The bench OPENS ON a condition and
  // a condition you are looking at is one you have seen, which is Design's own
  // `seen: { winter: true }`. `head_counter.start` puts the 1 in the shipped
  // bytes; without it the page reads "0 of 5" until JS runs, and for ever in
  // what a crawler gets.
  if (!/\b1\b/.test(count.textContent)) {
    return "the bench opens on a condition and its readout says " +
      JSON.stringify(count.textContent);
  }
  // MRB-242: a stylesheet `display` on a `hidden` element beats the UA rule
  // and every condition on this bench would be on screen at once.
  var hid = w.querySelectorAll('[data-ab-envpanel][hidden]');
  if (!hid.length) { return "no condition panel ships hidden"; }
  for (var h = 0; h < hid.length; h++) {
    var el = hid[h], prev = el.style.display;
    el.style.display = '';
    var shown = getComputedStyle(el).display;
    el.style.display = prev;
    if (shown !== 'none') {
      return "MRB-242: a condition panel ships `hidden` and the stylesheet " +
        "gives it display:" + shown + ", which beats the UA [hidden] rule";
    }
  }
  var open = w.querySelectorAll('[data-ab-envpanel]:not([hidden])');
  if (open.length !== 1) {
    return "the bench opens with " + open.length + " conditions showing";
  }
  // ⚖️ EVERY CONDITION'S PANEL IS IN THE DOCUMENT, so the shipped bytes carry
  // every verdict and every per-subject reason rather than the runtime writing
  // them in. Checked by counting reasons against tabs × subjects.
  var subjects = open[0].querySelectorAll('.ks3-ab-row').length;
  if (subjects < 2) { return "the column holds " + subjects + " subject(s)"; }
  var whys = w.querySelectorAll('.ks3-ab-why').length;
  if (whys !== subjects * tabs.length) {
    return "the bench ships " + whys + " reasons for " + tabs.length +
      " conditions × " + subjects + " subjects";
  }
  if (w.querySelectorAll('.ks3-ab-verdict').length !== tabs.length) {
    return "the bench ships " + w.querySelectorAll('.ks3-ab-verdict').length +
      " verdicts for " + tabs.length + " conditions";
  }
  // ⛔ AND NO SCIENCE-BEARING STRING RIDES AN ATTRIBUTE. Everything above is
  // static markup; the runtime only unhides.
  //
  // Now switch. One press per world, and the stage may not flip early.
  var opened = open[0].getAttribute('data-ab-envpanel');
  var order = [];
  for (var i = 0; i < tabs.length; i++) {
    var id = tabs[i].getAttribute('data-ab-env');
    if (id !== opened) { order.push(tabs[i]); }
  }
  for (var k = 0; k < need - 1; k++) {
    if (sec.getAttribute('data-stage-done') === '1') {
      return "the stop ticked after " + (k + 1) + " of " + need + " conditions";
    }
    order[k].click();
    var live = w.querySelectorAll('[data-ab-envpanel]:not([hidden])');
    if (live.length !== 1 ||
        live[0].getAttribute('data-ab-envpanel') !==
          order[k].getAttribute('data-ab-env')) {
      return "a condition was chosen and the panel did not follow it";
    }
    if (order[k].getAttribute('aria-pressed') !== 'true') {
      return "the chosen condition is not pressed";
    }
    if (w.querySelectorAll('[data-ab-env][aria-pressed="true"]').length !== 1) {
      return "two conditions are pressed at once";
    }
  }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return need + " conditions were tried and the stop did not tick";
  }
  // ⚠️ `seen` NEVER SHRINKS. Going back to a world already visited must not
  // reduce the count, and must not untick the stop — two rail entries read
  // this marker (MRB-249), and MRB-208 ruled the rail records participation.
  var was = count.textContent;
  order[0].click();
  if (count.textContent !== was) {
    return "returning to a condition already seen changed the count from " +
      JSON.stringify(was) + " to " + JSON.stringify(count.textContent);
  }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "returning to a condition already seen unticked the stop";
  }
  // ⛔ MRB-196 R10 — the bench marks nothing. No option button anywhere in
  // this instrument may take a verdict class.
  if (w.querySelector('.ks3-option.is-correct, .ks3-option.is-wrong, .ks3-option.is-spent')) {
    return "MRB-196 R10: the bench marked a condition button";
  }
  // ⛔⛔ AND THE TIE. Find the column whose printed figures have no unique
  // maximum, open it, and leave it open for the two driven rows above. It must
  // mark NOTHING — no `data-ab-rank` anywhere in it, on a figure or on a bar.
  var tied = null;
  for (var e2 = 0; e2 < tabs.length; e2++) {
    var pid = tabs[e2].getAttribute('data-ab-env');
    var panel = w.querySelector('[data-ab-envpanel="' + pid + '"]');
    var nums = Array.prototype.map.call(
      panel.querySelectorAll('.ks3-ab-chance'),
      function (x) { return parseInt(x.textContent, 10); });
    var hi = Math.max.apply(null, nums), lo = Math.min.apply(null, nums);
    var uniq = nums.filter(function (n) { return n === hi; }).length === 1 &&
               nums.filter(function (n) { return n === lo; }).length === 1 &&
               hi !== lo;
    var marked = panel.querySelectorAll('[data-ab-rank]').length;
    if (uniq) {
      // A column with two clean ends marks exactly two things: one figure and
      // its bar for the best, one figure and its bar for the worst.
      if (marked !== 4) {
        return "condition " + pid + " has a unique best and a unique worst " +
          "and carries " + marked + " marked element(s), not 4";
      }
      if (panel.querySelectorAll('[data-ab-rank="best"]').length !== 2 ||
          panel.querySelectorAll('[data-ab-rank="worst"]').length !== 2) {
        return "condition " + pid + " marks a best or a worst on only one of " +
          "the figure and the bar";
      }
    } else {
      if (marked !== 0) {
        return "condition " + pid + " has no unique extreme and still marks " +
          marked + " element(s) — Design's own renderer paints four green " +
          "'best here' winners on the disease column under a verdict reading " +
          "'None of the visible variations helps.'";
      }
      tied = tabs[e2];
    }
  }
  if (!tied) {
    return "no column on this bench ties, so the suppression rule that the " +
      "disease panel exists to prove is untested here";
  }
  tied.click();
  return null;
})()
""",
    # ⚖️⚖️ TEN GENERATIONS, A BARK SWITCH, A RESET AND FIFTY GENERATIONS OF
    # THE CONTROL — because every one of those is a claim this bench makes and
    # none of them is visible in the markup.
    #
    # What is proved here: nothing ticks on load; the recurrence moves the
    # population and the stage flips on Design's own `gen >= 10`; switching
    # bark does NOT reset the population (which is what lets a student watch it
    # come back, and is the best thing on the bench); the reset shows
    # `notes.reset` and NOT `notes.start` — the gen-0 defect in the delivered
    # bytes, where a fifty-fifty population sits under "Nine moths in ten are
    # pale"; the stop stays ticked through a reset (MRB-208); and the control
    # bark does not move by so much as a rounding pixel over fifty
    # generations, which is the panel that proves the other two show selection
    # rather than an animation.
    "b11-generations-run": r"""
(function () {
  var sec = document.querySelector('[data-nrblock]');
  if (!sec) { return "no selection runner on the page"; }
  if (sec.getAttribute('data-stage-done') === '1') { return "the stop ticked on load"; }
  var w = sec.querySelector('[data-nr]');
  if (!w) { return "the practical shell rendered without the instrument"; }
  var M; try { M = JSON.parse(w.getAttribute('data-model')); } catch (x) { M = null; }
  if (!M || !M.barks) { return "the bench shipped no model"; }
  var need = Number(w.getAttribute('data-threshold'));
  if (!need) { return "the bench declares no completion threshold"; }
  var count = sec.querySelector('[data-count]');
  if (!count) { return "the bench ships no head readout"; }
  if (count.textContent.indexOf('{') >= 0) {
    return "the head readout shipped an unfilled placeholder: " + count.textContent;
  }
  // ⚠️ THE TRAILING SPACE. `gen_label` is "generation " and the composition
  // adds no separator of its own; a doubled space would ship "generation  7"
  // and no gate but this one would see it. B10's `zoom-bench` shipped the
  // mirror image ("level1of6") until the spaces went back.
  if (/\s\s/.test(count.textContent)) {
    return "the head readout doubled a separator: " + JSON.stringify(count.textContent);
  }
  // ⛔ THE BENCH OPENS ON THE BARK THE MODEL NAMES, WHICH IS NOT THE FIRST.
  // Design's state is `bark: 'sooty'`, the second entry — the lesson opens in
  // industrial Britain because that is where one press of *Ten generations*
  // shows the sweep. A silent fallback to the first bark opens the lesson on
  // the wrong world and nothing else anywhere says a word.
  var live = w.querySelectorAll('[data-nr-bark][aria-pressed="true"]');
  if (live.length !== 1) { return live.length + " barks are pressed at once"; }
  if (live[0].getAttribute('data-nr-bark') !== M.opens_on) {
    return "the bench opens on " + live[0].getAttribute('data-nr-bark') +
      " and the model says " + M.opens_on;
  }
  var first = w.querySelector('[data-nr-bark]').getAttribute('data-nr-bark');
  if (first === M.opens_on) {
    return "the opening bark IS the first bark, so this assertion proves " +
      "nothing about the fallback it exists to catch";
  }
  // Exactly one control, and it is what makes the third panel a control.
  var controls = 0, key;
  for (key in M.barks) {
    if (Object.prototype.hasOwnProperty.call(M.barks, key) &&
        M.barks[key].control) { controls += 1; }
  }
  if (controls !== 1) { return "the bench declares " + controls + " control bark(s)"; }
  // MRB-242 — a stylesheet `display` on a hidden column beats the UA rule, and
  // the column rule below IS a `display: flex`. All twenty-four would paint.
  var hid = w.querySelectorAll('[data-nr-col][hidden]');
  if (!hid.length) { return "no history column ships hidden"; }
  if (getComputedStyle(hid[0]).display !== 'none') {
    return "MRB-242: a history column ships `hidden` and the stylesheet gives " +
      "it display:" + getComputedStyle(hid[0]).display;
  }
  if (w.querySelectorAll('[data-nr-col]:not([hidden])').length !== 1) {
    return "the bench opens with more than the starting generation drawn";
  }
  // Six note branches in the document, one shown, none written in by the
  // runtime: every sentence this bench can say is in the shipped bytes.
  if (w.querySelectorAll('[data-nr-note]').length !== 6) {
    return "the bench ships " + w.querySelectorAll('[data-nr-note]').length +
      " note branches and there are six";
  }
  function shownNote() {
    var n = w.querySelectorAll('[data-nr-note]:not([hidden])');
    return n.length === 1 ? n[0].getAttribute('data-nr-note') : ('x' + n.length);
  }
  if (shownNote() !== 'start') {
    return "the bench opens on note " + shownNote() + " and not `start`";
  }
  function pct(which) {
    var f = w.querySelector('[data-nr-series="' + which + '"]');
    return parseInt(f.textContent.replace(/[^0-9]/g, ''), 10);
  }
  var pale0 = pct('pale');
  var ten = w.querySelector('[data-nr-run="' + need + '"]');
  if (!ten) { return "the bench has no button that runs " + need + " generations"; }
  ten.click();
  if (sec.getAttribute('data-stage-done') !== '1') {
    return need + " generations were run and the stop did not tick";
  }
  if (pct('pale') === pale0) {
    return need + " generations on the opening bark and the population did not move";
  }
  if (pct('pale') + pct('dark') !== 100) {
    return "the two figures read " + pct('pale') + " and " + pct('dark');
  }
  if (w.querySelectorAll('[data-nr-col]:not([hidden])').length !== need + 1) {
    return "a " + need + "-generation run drew " +
      w.querySelectorAll('[data-nr-col]:not([hidden])').length + " columns";
  }
  // ⚖️ SWITCHING BARK DOES NOT RESET THE POPULATION. Without this a student
  // cannot run it sooty, switch to clean and watch it come back — which is
  // the one demonstration on the page that selection has no memory.
  var held = pct('pale');
  var other = null, tabs = w.querySelectorAll('[data-nr-bark]');
  for (var i = 0; i < tabs.length; i++) {
    var bid = tabs[i].getAttribute('data-nr-bark');
    if (bid !== M.opens_on && !M.barks[bid].control) { other = tabs[i]; }
  }
  if (!other) { return "the bench offers no second bark that selects"; }
  other.click();
  if (pct('pale') !== held) {
    return "switching bark reset the population from " + held + "% to " + pct('pale') + "%";
  }
  if (Number(count.textContent.replace(/[^0-9]/g, '')) !== need) {
    return "switching bark moved the generation counter";
  }
  // ⛔⛔ THE GEN-0 FIX. Design's reset sets `pale: 0.5, gen: 0` and her
  // `notes.start` fires on `gen === 0` alone, so her page prints "Nine moths
  // in ten are pale" over a fifty-fifty population. The port gates `start` on
  // the STARTING fraction and authors `reset` for the other one.
  var resetBtn = w.querySelector('[data-nr-reset]');
  if (!resetBtn) { return "the bench has no reset"; }
  resetBtn.click();
  if (Number(count.textContent.replace(/[^0-9]/g, '')) !== 0) {
    return "the reset did not return the bench to generation 0";
  }
  if (pct('pale') !== Math.round(M.reset * 100)) {
    return "the reset left the population at " + pct('pale') + "%";
  }
  if (shownNote() !== 'reset') {
    return "after the reset the bench shows note `" + shownNote() + "` — the " +
      "delivered page shows `start`, which reads 'Nine moths in ten are pale' " +
      "over a fifty-fifty population";
  }
  // MRB-208 — the rail records participation. Resetting is using the bench.
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "the reset unticked a stop the student had already earned";
  }
  // ⚑⚑ THE CONTROL DOES NOT CREEP, AND IT IS TESTED OFF A HALF.
  //
  // ⚠️ FIFTY-FIFTY IS THE ONE FRACTION THAT CANNOT FAIL. At p = 0.5 with equal
  // rates, `0.5·s / (0.5·s + 0.5·s)` is exactly 0.5 in floating point whichever
  // way it is written — so a control tested straight after the reset proves
  // nothing at all, and this drive passed a mutation that removed the
  // short-circuit entirely until it was moved off the half. One selecting
  // generation first, which lands the population on a fraction with a long
  // tail; then fifty on the control, which is more than the history holds, so
  // every drawn column is a post-switch one.
  // ⚠️⚠️ THE STARTING FRACTION IS CHOSEN, NOT TAKEN. Almost every fraction on
  // this bench is a fixed point of the naive arithmetic as well as of the
  // short-circuit — `p·s / (p·s + (1−p)·s)` comes back bit-for-bit `p` for
  // 0.5, for 0.9, and for most of what a run lands on — so a control tested
  // from the reset value passes whichever way the step is written and proves
  // nothing. This drive did exactly that until it was measured: the mutation
  // that removes the short-circuit went green.
  //
  // Ten generations on the PALE-FAVOURED bark from the reset lands the
  // population on 0.998273425228992, which is one of the fractions the naive
  // arithmetic does NOT hold — fifty control steps move it to
  // …9919. Deliberately chosen, and named here so a later edit cannot
  // "simplify" the route back to something that passes for nothing.
  var sel = null, ctl = null;
  for (var j = 0; j < tabs.length; j++) {
    var bid2 = tabs[j].getAttribute('data-nr-bark');
    if (M.barks[bid2].control) { ctl = tabs[j]; }
    else if (M.barks[bid2].pale_favoured) { sel = tabs[j]; }
  }
  if (!ctl || !sel) {
    return "the bench has no control bark or no pale-favoured selecting one";
  }
  sel.click();
  ten.click();
  ctl.click();
  //
  // ⚠️ AND IT IS READ OFF `data-nr-pale`, NOT OFF THE DRAWN HEIGHT. A
  // percentage set through `style.height` comes back out of the CSSOM
  // re-serialised to four decimal places, so a difference in the sixteenth
  // digit — which is the whole of what a creeping control is — is invisible in
  // the drawn value. The instrument writes the model's own fraction beside it
  // for exactly this reason.
  var live0 = w.querySelectorAll('[data-nr-col]:not([hidden])');
  var h0 = live0[live0.length - 1].getAttribute('data-nr-pale');
  if (!h0) {
    return "the bench draws its history without recording the fraction, so " +
      "the control's exactness cannot be measured at all";
  }
  if (h0 === '0.5' || h0 === '0.9') {
    return "the control is being tested from " + h0 + ", which is a fixed " +
      "point of the naive arithmetic as well as of the short-circuit — the " +
      "assertion below would pass whichever way the step is written";
  }
  for (var k = 0; k < 5; k++) { ten.click(); }
  var drawn = w.querySelectorAll('[data-nr-col]:not([hidden])');
  if (drawn.length !== M.history) {
    return "fifty generations drew " + drawn.length + " columns and the " +
      "history is " + M.history;
  }
  for (var c = 0; c < drawn.length; c++) {
    if (drawn[c].getAttribute('data-nr-pale') !== h0) {
      return "the control moved: column " + c + " is " +
        drawn[c].getAttribute('data-nr-pale') + " where the start was " + h0;
    }
  }
  if (shownNote() !== 'control') {
    return "fifty generations on the control bark and the bench shows note `" +
      shownNote() + "`";
  }
  if (w.querySelector('.ks3-option.is-correct, .ks3-option.is-wrong, .ks3-option.is-spent')) {
    return "MRB-196 R10: the bench marked a bark button";
  }
  // Leave the bench on a full history for the driven row above.
  return null;
})()
""",
    # ⚖️ FOUR COMBINATIONS, AND THE UNIT IS THE PAIR. What Design counts is
    # `seen[species + '-' + pressure]`, so a bench that counted axis presses
    # would tick its stage for a student who had looked at four species under
    # ONE pressure and never watched a row change — which is the lesson. Proved
    # here by moving one axis at a time and reading the count.
    #
    # Also proved: the singular ("1 combination tried") in the SHIPPED BYTES,
    # the twenty outcome texts all being present rather than composed, and the
    # three bands resolving to three different colours. The drive ends on a
    # top-band cell for the two driven rows above.
    "b11-combinations-tried": r"""
(function () {
  var sec = document.querySelector('[data-pbblock]');
  if (!sec) { return "no pressure bench on the page"; }
  if (sec.getAttribute('data-stage-done') === '1') { return "the stop ticked on load"; }
  var w = sec.querySelector('[data-pb]');
  if (!w) { return "the practical shell rendered without the instrument"; }
  var need = Number(w.getAttribute('data-threshold'));
  if (!need) { return "the bench declares no completion threshold"; }
  var sp = w.querySelectorAll('[data-pb-species]');
  var pr = w.querySelectorAll('[data-pb-pressure]');
  if (sp.length < 2 || pr.length < 2) {
    return "the bench offers " + sp.length + " species and " + pr.length + " pressures";
  }
  var cells = w.querySelectorAll('[data-pb-cell]');
  // ⚠️ EVERY COMBINATION IS IN THE DOCUMENT. Design's `OUTCOMES` is a full
  // grid of individually written prose — nothing generated, nothing
  // templated — so the count is the product and a shortfall is a cell that
  // would draw a number and a bar with nothing underneath.
  if (cells.length !== sp.length * pr.length) {
    return "the bench ships " + cells.length + " outcome cells for " +
      sp.length + " species × " + pr.length + " pressures";
  }
  var count = sec.querySelector('[data-count]');
  if (!count) { return "the bench ships no head readout"; }
  if (count.textContent.indexOf('{') >= 0) {
    return "the head readout shipped an unfilled placeholder: " + count.textContent;
  }
  // ⛔ THE `(s)` IS EXPANDED, IN THE SHIPPED BYTES. The author writes the noun
  // once as "combination(s) tried"; unsplit, the resting page reads
  // "1 combination(s) tried" — visible on screen, invisible to every gate that
  // does not open a browser.
  if (/\(s\)/.test(count.textContent)) {
    return "the head readout shipped an unexpanded plural marker: " +
      JSON.stringify(count.textContent);
  }
  if (!/\b1\b/.test(count.textContent)) {
    return "the bench opens on a pair and its readout says " +
      JSON.stringify(count.textContent);
  }
  var openedSingular = count.textContent;
  // MRB-242 — a stylesheet `display` on a hidden cell would put all twenty on
  // screen at once.
  var hid = w.querySelectorAll('[data-pb-cell][hidden]');
  if (!hid.length) { return "no outcome cell ships hidden"; }
  if (getComputedStyle(hid[0]).display !== 'none') {
    return "MRB-242: an outcome cell ships `hidden` and the stylesheet gives " +
      "it display:" + getComputedStyle(hid[0]).display;
  }
  if (w.querySelectorAll('[data-pb-cell]:not([hidden])').length !== 1) {
    return "the bench opens with more than one outcome on screen";
  }
  var open0 = w.querySelector('[data-pb-cell]:not([hidden])').getAttribute('data-pb-cell');
  if (open0 !== (w.getAttribute('data-opens-on') || '')) {
    return "the bench opens on " + open0 + " and declares " +
      w.getAttribute('data-opens-on');
  }
  // ⚖️ ONE AXIS AT A TIME, AND EACH MOVE IS A NEW PAIR. Move the pressure
  // three times without touching the species: four pairs, four counts, and
  // the stage ticks on the fourth.
  var moved = 0;
  for (var i = 0; i < pr.length && moved < need - 1; i++) {
    if (pr[i].getAttribute('aria-pressed') === 'true') { continue; }
    if (sec.getAttribute('data-stage-done') === '1') {
      return "the stop ticked after " + (moved + 1) + " of " + need + " combinations";
    }
    pr[i].click();
    moved += 1;
    if (w.querySelectorAll('[data-pb-cell]:not([hidden])').length !== 1) {
      return "a pressure was chosen and " +
        w.querySelectorAll('[data-pb-cell]:not([hidden])').length + " outcomes showed";
    }
    var want = w.querySelector('[data-pb-species][aria-pressed="true"]')
      .getAttribute('data-pb-species') + '|' + pr[i].getAttribute('data-pb-pressure');
    if (w.querySelector('[data-pb-cell]:not([hidden])').getAttribute('data-pb-cell') !== want) {
      return "the pressure changed and the outcome cell did not follow the PAIR";
    }
    if (w.querySelectorAll('[data-pb-pressure][aria-pressed="true"]').length !== 1) {
      return "two pressures are pressed at once";
    }
  }
  if (moved !== need - 1) { return "could not reach " + need + " combinations"; }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return need + " combinations were tried and the stop did not tick";
  }
  // The plural arrived, and it is a different string from the singular.
  if (count.textContent === openedSingular) {
    return "the readout says the same thing at 1 and at " + need;
  }
  if (/\(s\)/.test(count.textContent)) {
    return "the plural readout still carries the marker: " + count.textContent;
  }
  // ⚠️ AND `seen` NEVER SHRINKS. Returning to the opening pair must not reduce
  // the count nor untick the stop — two rail entries read this marker.
  var was = count.textContent;
  var back = w.querySelector('[data-pb-pressure="' + open0.split('|')[1] + '"]');
  back.click();
  if (count.textContent !== was) {
    return "returning to a pair already seen changed the count from " +
      JSON.stringify(was) + " to " + JSON.stringify(count.textContent);
  }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "returning to a pair already seen unticked the stop";
  }
  // ⚖️⚖️ AND THE UNIT IS THE PAIR, WHICH IS WHAT THIS PROVES. Everything above
  // moved ONE axis, so a bench that counted pressure presses would have kept
  // pace with a bench that counted pairs. Move the SPECIES now, with the
  // pressure held: the pair is new, so the count must rise. Keyed on either
  // axis alone it does not, and the stage then ticks for a student who looked
  // at four species under one pressure and never watched a row change.
  var before = Number(count.textContent.replace(/[^0-9]/g, ''));
  var otherSp = null;
  for (var s3 = 0; s3 < sp.length; s3++) {
    if (sp[s3].getAttribute('aria-pressed') !== 'true') { otherSp = sp[s3]; }
  }
  if (!otherSp) { return "every species is pressed at once"; }
  otherSp.click();
  if (Number(count.textContent.replace(/[^0-9]/g, '')) !== before + 1) {
    return "a new SPECIES under a pressure already seen did not count as a " +
      "new combination — the unit is the pair, not the button";
  }
  // ⛔ MRB-196 R10 — no tab on either axis takes a verdict class.
  if (w.querySelector('.ks3-option.is-correct, .ks3-option.is-wrong, .ks3-option.is-spent')) {
    return "MRB-196 R10: the bench marked an axis button";
  }
  // ⚑⚑ THREE BANDS, THREE COLOURS, AND ALL THREE REACHABLE. A bench whose
  // cells all fell in one band would draw twenty rows in one colour and the
  // band rule would be dead CSS that greps clean.
  var bands = {};
  for (var c = 0; c < cells.length; c++) {
    var el = cells[c].querySelector('.ks3-pb-outpct');
    bands[el.getAttribute('data-pb-band')] = true;
    var bar = cells[c].querySelector('.ks3-pb-bar');
    if (bar.getAttribute('data-pb-band') !== el.getAttribute('data-pb-band')) {
      return "cell " + cells[c].getAttribute('data-pb-cell') +
        " paints its figure and its bar in different bands";
    }
  }
  if (!bands.ok || !bands.mid || !bands.bad) {
    return "the twenty cells reach bands " + Object.keys(bands).join(",") +
      " — a band with no cell is a colour rule nothing on the page can show";
  }
  // Leave the bench on a TOP-band cell for the two driven rows above.
  for (var s2 = 0; s2 < sp.length; s2++) {
    for (var p2 = 0; p2 < pr.length; p2++) {
      var key = sp[s2].getAttribute('data-pb-species') + '|' +
                pr[p2].getAttribute('data-pb-pressure');
      var cell = w.querySelector('[data-pb-cell="' + key + '"]');
      if (cell.querySelector('.ks3-pb-outpct').getAttribute('data-pb-band') === 'ok') {
        sp[s2].click(); pr[p2].click();
        return null;
      }
    }
  }
  return "no cell on this bench falls in the top band";
})()
""",
    # ⚖️⚖️ THE BLIGHT RELEASED ON THE CLONE FIELD, WHICH RETURNS EXACTLY ZERO.
    # `resistant: 0` over `varieties: 1` is zero along every arithmetic path,
    # and that number is the payoff of the lesson — the Irish potato crop, the
    # Gros Michel. Checked as an integer and not as a bar width, because a
    # rounding that produced one survivor in a thousand would draw an
    # identical bar.
    #
    # Also proved: the resting field is PLANTED AND WHOLE (a full green bar at
    # total-of-total, which is what makes the release mean something); the
    # verdict arrives only on release; switching field re-arms the blight;
    # *Clear the field* clears the release and NOT the tally; and the stage
    # ticks on Design's own `tried >= 2`.
    "b11-blight-released": r"""
(function () {
  var sec = document.querySelector('[data-bbblock]');
  if (!sec) { return "no blight bench on the page"; }
  if (sec.getAttribute('data-stage-done') === '1') { return "the stop ticked on load"; }
  var w = sec.querySelector('[data-bb]');
  if (!w) { return "the practical shell rendered without the instrument"; }
  var need = Number(w.getAttribute('data-threshold'));
  if (!need) { return "the bench declares no completion threshold"; }
  var tabs = w.querySelectorAll('[data-bb-field]');
  if (tabs.length < need) {
    return "the bench plants " + tabs.length + " field(s) and needs " + need;
  }
  var run = w.querySelector('[data-bb-run]');
  var clear = w.querySelector('[data-bb-clear]');
  if (!run || !clear) { return "the bench ships without its two controls"; }
  var count = sec.querySelector('[data-count]');
  if (!count) { return "the bench ships no head readout"; }
  if (count.textContent.indexOf('{') >= 0 || /\(s\)/.test(count.textContent)) {
    return "the head readout shipped an unfilled placeholder or an " +
      "unexpanded plural: " + JSON.stringify(count.textContent);
  }
  var zeroLabel = count.textContent;
  // ⚠️ THE RESTING FIELD IS PLANTED AND UNTOUCHED. The release ships LIVE and
  // the verdict ships hidden — Design disables the button only once it has
  // been pressed.
  if (run.disabled) { return "the release button ships already spent"; }
  if (w.querySelector('[data-bb-verdict]:not([hidden])')) {
    return "a verdict is on screen before the blight was released";
  }
  var open = w.querySelectorAll('[data-bb-fieldpanel]:not([hidden])');
  if (open.length !== 1) { return "the bench opens with " + open.length + " fields showing"; }
  function survRow() {
    return w.querySelector('[data-bb-fieldpanel]:not([hidden]) [data-bb-surv]:not([hidden])');
  }
  var before = survRow();
  if (!before || before.getAttribute('data-bb-surv') !== 'before') {
    return "the resting field does not show its unblighted harvest";
  }
  if (before.querySelector('.ks3-bb-bar').style.width !== '100%') {
    return "the unblighted field is drawn at " +
      before.querySelector('.ks3-bb-bar').style.width + " and every plant is standing";
  }
  // ⚖️ THREE BARS, AND THE THIRD IS THE COST. A bench that drew survival and
  // variation but not yield would teach that variation is free.
  var bars = w.querySelectorAll('[data-bb-fieldpanel]:not([hidden]) .ks3-bb-row:not([hidden])');
  if (bars.length !== 3) {
    return "the field draws " + bars.length + " bars and there are three — " +
      "what survived, how much variation went in, and what it yields";
  }
  // MRB-242, on both the hidden panels and the hidden survivor rows.
  var hid = w.querySelectorAll('[data-bb-fieldpanel][hidden], [data-bb-surv][hidden], [data-bb-verdict][hidden]');
  if (!hid.length) { return "nothing on this bench ships hidden"; }
  for (var h = 0; h < hid.length; h++) {
    if (getComputedStyle(hid[h]).display !== 'none') {
      return "MRB-242: " + hid[h].className + " ships `hidden` and the " +
        "stylesheet gives it display:" + getComputedStyle(hid[h]).display;
    }
  }
  // ⛔⛔ RELEASE IT. The opening field is the one with no resistant variety.
  run.click();
  if (!run.disabled) { return "the blight was released and the button stayed live"; }
  if (run.textContent.trim() === w.getAttribute('data-run-label').trim()) {
    return "the blight has passed through and the button still reads " +
      JSON.stringify(run.textContent);
  }
  var after = survRow();
  if (!after || after.getAttribute('data-bb-surv') !== 'after') {
    return "the blight was released and the harvest did not change";
  }
  // The integer, not the bar. A rounding that left one plant in a thousand
  // would draw a bar of the same width and be a different lesson.
  var nums = after.querySelector('.ks3-bb-value').textContent.match(/\d+/g) || [];
  if (nums.length < 2) {
    return "the survivor row reads " +
      JSON.stringify(after.querySelector('.ks3-bb-value').textContent);
  }
  if (Number(nums[0]) !== 0) {
    return "the clone field returned " + nums[0] + " survivor(s) of " + nums[1] +
      " — `resistant: 0` over `varieties: 1` is zero along every arithmetic path";
  }
  if (after.querySelector('.ks3-bb-value').getAttribute('data-bb-band') !== 'none') {
    return "a zero harvest is in band " +
      after.querySelector('.ks3-bb-value').getAttribute('data-bb-band') +
      " — zero is its own band, not the bottom of one";
  }
  if (!w.querySelector('[data-bb-verdict]:not([hidden])')) {
    return "the blight passed through and no verdict arrived";
  }
  if (/[{}]/.test(w.querySelector('[data-bb-verdict]:not([hidden])').textContent)) {
    return "the verdict shipped an unfilled placeholder";
  }
  if (count.textContent === zeroLabel) {
    return "a field was tested and the readout still says " + JSON.stringify(zeroLabel);
  }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked after 1 of " + need + " fields";
  }
  // ⚖️ SWITCHING FIELD RE-ARMS THE BLIGHT, which is Design's own tab handler
  // (`{ field: x.id, released: false }`).
  //
  // ⚠️ TESTED BEFORE THE CLEAR, AND THAT ORDER IS THE ASSERTION. Clearing the
  // field also un-releases it, so a switch tested after a clear finds the
  // blight armed whether the tab handler re-arms it or not — this drive passed
  // a mutation that deleted the re-arm entirely until the two were reordered.
  var tallied = count.textContent;
  var second = null, opened = open[0].getAttribute('data-bb-fieldpanel');
  for (var i = 0; i < tabs.length; i++) {
    if (tabs[i].getAttribute('data-bb-field') !== opened) { second = tabs[i]; }
  }
  second.click();
  if (run.disabled) { return "a new field was planted and the blight was already spent"; }
  if (w.querySelector('[data-bb-verdict]:not([hidden])')) {
    return "a new field was planted with the previous field's verdict on it";
  }
  // ⚖️ AND *Clear the field* CLEARS THE RELEASE AND NOT THE TALLY. MRB-208:
  // the rail records participation, and clearing a field is using the bench.
  run.click();
  clear.click();
  if (run.disabled) { return "the field was cleared and the blight stayed spent"; }
  if (w.querySelector('[data-bb-verdict]:not([hidden])')) {
    return "the field was cleared and its verdict stayed on screen";
  }
  if (Number(count.textContent.replace(/[^0-9]/g, '')) !== 2) {
    return "clearing a field un-counted it: the readout reads " +
      JSON.stringify(count.textContent) + " after two fields were tested";
  }
  if (count.textContent === tallied) {
    return "a second field was tested and the readout still says " +
      JSON.stringify(tallied);
  }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return need + " fields were tested and the stop did not tick";
  }
  var pluralised = count.textContent;
  if (/\(s\)/.test(pluralised)) {
    return "the plural readout still carries the marker: " + pluralised;
  }
  if (pluralised === tallied) {
    return "the readout says the same thing at 1 and at " + need + " fields";
  }
  // Re-testing a field already tested must not double-count it.
  second.click();
  run.click();
  if (count.textContent !== pluralised) {
    return "releasing the blight twice on one field counted it twice";
  }
  if (w.querySelector('.ks3-option.is-correct, .ks3-option.is-wrong, .ks3-option.is-spent')) {
    return "MRB-196 R10: the bench marked a field button";
  }
  // Leave the bench on the zero-harvest field for the driven rows above.
  w.querySelector('[data-bb-field="' + opened + '"]').click();
  run.click();
  return null;
})()
""",
    # ⚖️ THE DRAWN MOTH PAIR, STRUCTURALLY. What the four rows above cannot
    # say is that the two barks differ by PATTERN as well as by tone, that the
    # same two moths appear on both, and that every one of them is labelled —
    # which is the whole of what makes the drawing honest as well as legible.
    #
    # ⊖ This drive runs only once b11-02's figure record is wired; until then
    # its rows are parked and it never fires. Written now, with the drawer, so
    # that un-parking is a deletion rather than an afternoon.
    "b11-moth-pair": r"""
(function () {
  var svg = document.querySelector('.ks3-figure-drawn svg');
  if (!svg) { return "no drawn figure on the page"; }
  if (!svg.querySelector('title') || !svg.querySelector('desc')) {
    return "the drawing ships without a <title> or a <desc>";
  }
  var barks = svg.querySelectorAll('.ks3-moth-bark');
  if (barks.length !== 2) { return "the drawing has " + barks.length + " panels"; }
  if (barks[0].getAttribute('data-bark') === barks[1].getAttribute('data-bark')) {
    return "both panels draw the same bark";
  }
  // ⚑ PATTERN, NOT ONLY TONE. Mottle is a different KIND of mark from a
  // streak, and that is what makes the two panels tell apart for a reader who
  // cannot separate the tones.
  var mottle = svg.querySelectorAll('.ks3-moth-mottle').length;
  var streak = svg.querySelectorAll('.ks3-moth-streak').length;
  if (!mottle || !streak) {
    return "the two barks carry " + mottle + " mottle and " + streak +
      " streak marks — they differ by tone alone";
  }
  var moths = svg.querySelectorAll('.ks3-moth');
  if (moths.length !== 4) {
    return "the drawing carries " + moths.length + " moths and a pair of " +
      "panels showing the same two moths is four";
  }
  var pale = svg.querySelectorAll('.ks3-moth[data-moth-tone="pale"]').length;
  var dark = svg.querySelectorAll('.ks3-moth[data-moth-tone="dark"]').length;
  if (pale !== 2 || dark !== 2) {
    return "the panels carry " + pale + " pale and " + dark + " dark moths — " +
      "the claim is that NOTHING ABOUT THE MOTHS CHANGED and only the " +
      "background did, so each panel holds one of each";
  }
  // ⛔ EVERY MOTH IS LABELLED, twice: its name, and a written note saying how
  // easy it is to see there. Never colour-alone.
  if (svg.querySelectorAll('.ks3-moth-label').length !== 4 ||
      svg.querySelectorAll('.ks3-moth-note').length !== 4) {
    return "the drawing labels " + svg.querySelectorAll('.ks3-moth-label').length +
      " moths and annotates " + svg.querySelectorAll('.ks3-moth-note').length;
  }
  // ⚠️ AND NO PAINT RIDES A PRESENTATION ATTRIBUTE. `fill="var(--ks3-ink)"` is
  // not a valid <paint>; the attribute is dropped and the element renders
  // opaque black with every token grep still clean.
  var painted = svg.querySelectorAll('[fill]');
  for (var i = 0; i < painted.length; i++) {
    if (/var\(/.test(painted[i].getAttribute('fill'))) {
      return "an element paints through a `fill` attribute: " +
        painted[i].getAttribute('fill') + " — a custom property is not a " +
        "valid SVG paint and the element will render opaque black";
    }
  }
  return null;
})()
""",
    # ═══ END B11 drives ═══

    "b7-chain-traced": r"""
(function () {
  var sec = document.querySelector('[data-tbblock]');
  if (!sec) { return "no trace bench on the page"; }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on load";
  }
  var w = sec.querySelector('[data-tb]');
  if (!w) { return "the practical shell rendered without the instrument"; }
  var tabs = w.querySelectorAll('[data-tb-food]');
  if (tabs.length < 2) {
    return "the plate offers " + tabs.length + " food(s)";
  }
  if (!/class="[^"]*\bks3-option\b/.test(sec.innerHTML)) {
    return "the food tabs are not server-rendered options";
  }
  var panels = w.querySelectorAll('.ks3-tb-food:not([hidden])');
  if (panels.length !== 1) {
    return "the bench opens with " + panels.length + " food panels showing";
  }
  var cascade = w.querySelectorAll(
    '.ks3-tb-food[hidden], .ks3-tb-verdict[hidden], .ks3-tb-note[hidden]');
  for (var h = 0; h < cascade.length; h++) {
    var el = cascade[h], prev = el.style.display;
    el.style.display = '';
    var shown = getComputedStyle(el).display;
    el.style.display = prev;
    if (shown !== 'none') {
      return "MRB-242: " + el.className + " ships `hidden` but the stylesheet " +
        "gives it display:" + shown + ", which beats the UA [hidden] rule";
    }
  }

  var panel = panels[0];
  var total = parseInt(panel.getAttribute('data-total'), 10);
  if (!(total >= 3)) { return "the opening chain has " + total + " link(s)"; }
  // ⚖️ THE FOOD IS ON THE PLATE AND NOTHING ELSE IS. One note showing, and the
  // rest of the chain drawn but dim — a student reads how far there is to go.
  if (panel.querySelectorAll('.ks3-tb-note:not([hidden])').length !== 1) {
    return "the chain opens with " +
      panel.querySelectorAll('.ks3-tb-note:not([hidden])').length +
      " notes showing; there must be exactly one";
  }
  if (panel.querySelectorAll('.ks3-tb-link').length !== total) {
    return "the chain declares " + total + " links and draws " +
      panel.querySelectorAll('.ks3-tb-link').length;
  }
  if (panel.querySelector('.ks3-tb-verdict:not([hidden])')) {
    return "the verdict landed before the chain was complete";
  }

  var back = w.querySelector('[data-tb-back]');
  if (!back) { return "the bench has no step control"; }
  for (var i = 1; i < total; i++) {
    if (back.disabled) {
      return "the step button locked at link " + i + " of " + total;
    }
    back.click();
    var shownNotes = panel.querySelectorAll('.ks3-tb-note:not([hidden])').length;
    if (shownNotes !== i + 1) {
      return "press " + i + " revealed " + shownNotes +
        " notes; each press reveals exactly one more";
    }
    if (i < total - 1 && panel.querySelector('.ks3-tb-verdict:not([hidden])')) {
      return "the verdict landed at link " + (i + 1) + " of " + total;
    }
  }
  if (!panel.querySelector('.ks3-tb-verdict:not([hidden])')) {
    return "the chain reached its producer and no verdict landed";
  }
  if (!back.disabled) {
    return "the chain is complete and the step button is still live";
  }
  var steps = panel.querySelector('[data-tb-steps]');
  if (steps && steps.textContent.indexOf('{') >= 0) {
    return "the steps line shipped an unfilled placeholder: " + steps.textContent;
  }
  if (steps && steps.textContent.indexOf(String(total - 1)) < 0) {
    return "a chain of " + total + " links reported " + steps.textContent;
  }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "a chain was traced to its producer and the stop did not tick";
  }
  var count = sec.querySelector('[data-count]');
  if (count && parseInt(count.getAttribute('data-total'), 10) !== total) {
    return "the head counter's denominator is " +
      count.getAttribute('data-total') + " and this chain has " + total +
      " links";
  }

  // ⚖️ SWITCHING FOOD RESTARTS THE CHAIN AND UNTELLS NOTHING. The chains are
  // deliberately different lengths, so the denominator has to move with the
  // tab; and Design's readout says "chain traced" from the moment ONE chain
  // has been walked, on every food after it.
  for (var q = 0; q < tabs.length; q++) {
    if (tabs[q].getAttribute('aria-pressed') === 'false') {
      tabs[q].click();
      var next = w.querySelector('.ks3-tb-food:not([hidden])');
      if (!next) { return "switching food left no panel showing"; }
      if (next.querySelectorAll('.ks3-tb-note:not([hidden])').length !== 1) {
        return "switching food did not restart the chain";
      }
      var nTotal = parseInt(next.getAttribute('data-total'), 10);
      if (count && parseInt(count.getAttribute('data-total'), 10) !== nTotal) {
        return "the head counter's denominator did not follow the tab";
      }
      if (sec.getAttribute('data-stage-done') !== '1') {
        return "switching food unticked a stop the student had reached";
      }
      break;
    }
  }
  // Put the opening food back, walked to its producer, so the measured state
  // is the one the rows describe.
  tabs[0].click();
  for (var j = 1; j < total; j++) { back.click(); }
  return "";
})()
""",
    # ═══ END B7 ═══ drives
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


_JS_HIDDEN_AUDIT = r"""
(function () {
  // Every element the GENERATOR wrote `hidden` on must actually be hidden when
  // the page loads. The UA stylesheet's `[hidden] { display: none }` is the
  // weakest rule in the cascade: ANY author `display` beats it at ANY
  // specificity, so a component that gives itself `display: flex` un-hides its
  // own hidden children and nothing anywhere says so.
  //
  // ⊕ GATE C — ASK THE CASCADE, NOT THE PAINTED PAGE.
  //
  // Reading computed `display` straight off the loaded document answers a
  // different question from the one this audit means to ask, and the
  // difference has already hidden a real defect. A chassis that draws itself
  // on load — B5's commit bench is the one that caught us — writes an INLINE
  // `display: none` through its own `setHidden()`. An inline declaration beats
  // every author rule at every specificity, so it MASKS whatever the
  // stylesheet says underneath it. Give `.ks3-b5c-opts` a `display: flex` in
  // `shared/ks3.css` and the page is correct the instant JS runs and broken
  // before it — eight option lists stacked open for a reader with JS off, or
  // for the moment between paint and script — and this audit, reading the
  // painted result, reports display:none and zero problems.
  //
  // So for each element: drop its inline `display` for the length of one
  // read, ask the cascade what it says on its own, and put the inline value
  // back exactly as it was (value AND priority — `el.style.display` as a
  // getter silently loses `!important`). Judge on the cascade's answer.
  //
  // The two findings are NOT the same defect and are reported apart:
  //   plain         — the stylesheet openly un-hides it; visible right now.
  //   inline-masked — it looks hidden only because JS wrote an inline value
  //                   over a stylesheet that un-hides it. Invisible to a
  //                   screenshot, invisible to computed style, and the exact
  //                   shape this audit was blind to.
  // This technique lived in ONE drive (the B5 commit bench's local check) and
  // covered one component on one page; here it covers every `[hidden]`
  // element on every page.
  var out = [], n = 0, masked = 0;
  var els = document.querySelectorAll("[hidden]");
  for (var i = 0; i < els.length; i++) {
    var el = els[i];
    n++;

    var painted = getComputedStyle(el).display;
    var inlineVal = el.style.getPropertyValue("display");
    var inlinePri = el.style.getPropertyPriority("display");

    // One read with the element's own inline `display` lifted out of the way.
    if (inlineVal) { el.style.removeProperty("display"); }
    var cascade = getComputedStyle(el).display;
    if (inlineVal) { el.style.setProperty("display", inlineVal, inlinePri); }

    if (cascade === "none") { continue; }

    // Name it the way an author would recognise it: the class that is most
    // likely carrying the offending `display` rule.
    var cls = (el.className && el.className.baseVal !== undefined)
      ? el.className.baseVal : (el.className || "");
    var name = el.tagName.toLowerCase() +
      (cls ? "." + String(cls).trim().split(/\s+/).join(".") : "");

    var isMasked = (painted === "none");
    if (isMasked) { masked++; }
    out.push(name +
             (isMasked
               ? " [INLINE-MASKED] looks hidden only because an inline " +
                 "display:" + (inlineVal || "none") + " was written over it; " +
                 "the stylesheet alone gives it display:" + cascade +
                 " — with JS off, or before JS runs, it is OPEN"
               : " [PLAIN] computes display:" + cascade) +
             (el.hasAttribute("data-step") ? " [staged reveal step]" : ""));
  }
  return { problems: out, checked: n, masked: masked };
})()
"""


def check_hidden_stays_hidden(page):
    """⊕ MRB-242 — an element that ships `hidden` must load hidden.

    This exists because the trap has now been laid six times in one stylesheet
    and shipped to students once. `.ks3-fifa-chipped` set `display: flex`, which
    beats the UA `[hidden] { display: none }` at any specificity, so b2-04's
    worked example rendered all four FIFA steps at once above a counter reading
    "Step 0 of 4" and a button with nothing left to do — a staged reveal with
    nothing staged, and no gate with anything to say about it.

    Asserted on the UNDRIVEN load, because that is the only moment the claim is
    unambiguous: after any click, some of these are meant to be showing.

    Returns (problems, info). Read-only — safe on the pass-1 page.
    """
    info = page.eval(_JS_HIDDEN_AUDIT)
    return (["HIDDEN: " + p for p in info["problems"]], info)


# ── GATE A: the `.ks3-dark p` specificity trap, made structural ────────────
#
# `shared/ks3.css` declares `.ks3-dark p { color: var(--ks3-on-dark-body) }`.
# That selector is (0,1,1). Every bare instrument text class — `.ks3-fit-badge`,
# `.ks3-plate-note`, `.ks3-tbench-why` — is (0,1,0), so on an ink-dark block the
# author's own colour LOSES, silently, and the text ships present, correct and
# invisible. There is no console error, no missing element, no failed selector:
# the component is rendered, the rule is in the sheet, and the paint is wrong.
#
# This has now happened TEN times in one stylesheet. The comment blocks at
# ks3.css:1256, :3422 and :3510 are three separate authors writing down the same
# discovery, each scoping their own instance and leaving the trap armed for the
# next one. Scoping an instance fixes a page. Only a gate fixes the trap.
#
# So this asks the question structurally, in the browser, on the undriven load:
# for every element inside a `.ks3-dark` subtree, which colour rule actually
# WINS — and did an author write a colour for this component that lost? If the
# winner is a generic descendant rule whose rightmost compound is a bare type
# (`.ks3-dark p`, `.ks3-dark h2`) and a losing matched selector's rightmost
# compound is a `.ks3-*` class the element really carries, that is the trap
# exactly: somebody meant this component to have its own colour and the generic
# on-dark rule beat them to it.
#
# Three things a naive version of this gets wrong, all of them mirrored from
# `ks3_mutation.py:209`'s `_JS_MUTATOR`, which already solved the same walk:
#
#   1. Grouping rules. `@media`, `@supports`, `@layer` and `@container` hold
#      their own `cssRules`. KS3 ships 25 `@media` blocks and the responsive
#      colour work lives inside them, so a top-level-only walk would miss the
#      rules that are actually painting at this viewport. Recursed — but a
#      grouping rule whose condition does NOT currently match is not in the
#      cascade at all, and counting it would invent losers that never ran.
#   2. Selector lists. `selectorText` is one string for `a, b, c`; each of the
#      three has its own specificity, and only the ones that match this element
#      are in the running. Split on TOP-LEVEL commas — a comma inside `:is(…)`
#      or `[attr="a,b"]` is not a list separator.
#   3. Selectors this engine cannot parse. `el.matches()` throws on an unknown
#      pseudo rather than returning false, and one such rule anywhere in the
#      sheet would take the whole audit down. Every match is guarded; an
#      unparseable selector is skipped and counted, never fatal.
#
# `!important` is honoured as its own cascade tier, because an author who
# reached for it DID win and reporting them as a loser would be a lie. An
# element carrying an inline `color` is skipped outright — inline is explicit
# author intent and beats every rule here anyway.
_JS_DARK_TEXT_SPECIFICITY = r"""
(function () {

  // ── selector-string helpers ───────────────────────────────────────────
  // A hand-rolled scanner rather than a regex: KS3 selectors carry attribute
  // values, functional pseudos and nested selector lists, and a regex that
  // handles those is a parser written badly.

  function skipString(s, i) {                 // s[i] is the opening quote
    var q = s[i]; i++;
    while (i < s.length) {
      if (s[i] === "\\") { i += 2; continue; }
      if (s[i] === q) { return i + 1; }
      i++;
    }
    return i;
  }

  function skipBalanced(s, i, open, close) {  // s[i] is `open`
    var depth = 0;
    while (i < s.length) {
      var ch = s[i];
      if (ch === "\\") { i += 2; continue; }
      if (ch === '"' || ch === "'") { i = skipString(s, i); continue; }
      if (ch === open) { depth++; }
      else if (ch === close) { depth--; if (depth === 0) { return i + 1; } }
      i++;
    }
    return i;
  }

  function isIdentChar(ch) {
    return /[A-Za-z0-9_\- -￿\\]/.test(ch);
  }

  function skipIdent(s, i) {
    while (i < s.length && isIdentChar(s[i])) {
      if (s[i] === "\\") { i += 2; } else { i++; }
    }
    return i;
  }

  // Split a selector LIST on top-level commas only.
  function splitList(s) {
    var out = [], start = 0, i = 0;
    while (i < s.length) {
      var ch = s[i];
      if (ch === "\\") { i += 2; continue; }
      if (ch === '"' || ch === "'") { i = skipString(s, i); continue; }
      if (ch === "(") { i = skipBalanced(s, i, "(", ")"); continue; }
      if (ch === "[") { i = skipBalanced(s, i, "[", "]"); continue; }
      if (ch === ",") { out.push(s.slice(start, i)); start = i + 1; }
      i++;
    }
    out.push(s.slice(start));
    var trimmed = [];
    for (var k = 0; k < out.length; k++) {
      var t = out[k].trim();
      if (t) { trimmed.push(t); }
    }
    return trimmed;
  }

  // Split a COMPLEX selector into its compounds, on top-level combinators
  // (descendant space, `>`, `+`, `~`). Returns the compounds in order.
  function compounds(sel) {
    var out = [], start = 0, i = 0;
    function flush(end) {
      var t = sel.slice(start, end).trim();
      if (t) { out.push(t); }
    }
    while (i < sel.length) {
      var ch = sel[i];
      if (ch === "\\") { i += 2; continue; }
      if (ch === '"' || ch === "'") { i = skipString(sel, i); continue; }
      if (ch === "(") { i = skipBalanced(sel, i, "(", ")"); continue; }
      if (ch === "[") { i = skipBalanced(sel, i, "[", "]"); continue; }
      if (ch === " " || ch === "\t" || ch === "\n" ||
          ch === ">" || ch === "+" || ch === "~") {
        flush(i);
        while (i < sel.length && /[\s>+~]/.test(sel[i])) { i++; }
        start = i;
        continue;
      }
      i++;
    }
    flush(sel.length);
    return out;
  }

  function rightmost(sel) {
    var c = compounds(sel);
    return c.length ? c[c.length - 1] : sel.trim();
  }

  // ── specificity, (a, b, c) ────────────────────────────────────────────
  // a = #ids
  // b = classes + attribute selectors + pseudo-classes
  // c = type selectors + pseudo-elements
  // `:where()` contributes nothing; `:is()`, `:not()` and `:has()` contribute
  // the specificity of their most specific argument (CSS Selectors 4).
  var LEGACY_PSEUDO_ELEMENTS = {
    "before": 1, "after": 1, "first-line": 1, "first-letter": 1
  };
  var MATCHES_ARG = {
    "is": 1, "not": 1, "has": 1, "matches": 1, "-webkit-any": 1, "any": 1
  };

  function maxSpec(list) {
    var best = [0, 0, 0];
    for (var i = 0; i < list.length; i++) {
      var s = specificity(list[i]);
      if (cmpSpec(s, best) > 0) { best = s; }
    }
    return best;
  }

  function specificity(sel) {
    var a = 0, b = 0, c = 0, i = 0;
    while (i < sel.length) {
      var ch = sel[i];
      if (ch === "\\") { i += 2; continue; }
      if (ch === '"' || ch === "'") { i = skipString(sel, i); continue; }
      if (ch === "#") { a++; i = skipIdent(sel, i + 1); continue; }
      if (ch === ".") { b++; i = skipIdent(sel, i + 1); continue; }
      if (ch === "[") { b++; i = skipBalanced(sel, i, "[", "]"); continue; }
      if (ch === ":") {
        var dbl = (sel[i + 1] === ":");
        var start = i + (dbl ? 2 : 1);
        var j = skipIdent(sel, start);
        var name = sel.slice(start, j).toLowerCase();
        var args = null;
        if (sel[j] === "(") {
          var k = skipBalanced(sel, j, "(", ")");
          args = sel.slice(j + 1, k - 1);
          j = k;
        }
        if (dbl || LEGACY_PSEUDO_ELEMENTS[name]) {
          c++;                                   // pseudo-element
        } else if (name === "where") {
          /* contributes nothing, by definition */
        } else if (MATCHES_ARG[name]) {
          if (args) {
            var m = maxSpec(splitList(args));
            a += m[0]; b += m[1]; c += m[2];
          }
        } else if (name === "nth-child" || name === "nth-last-child") {
          b++;
          if (args) {                            // `nth-child(2 of .foo)`
            var of = args.toLowerCase().indexOf(" of ");
            if (of >= 0) {
              var m2 = maxSpec(splitList(args.slice(of + 4)));
              a += m2[0]; b += m2[1]; c += m2[2];
            }
          }
        } else {
          b++;                                   // ordinary pseudo-class
        }
        i = j;
        continue;
      }
      if (ch === "*" || ch === ">" || ch === "+" || ch === "~" ||
          ch === "," || ch === "|" || /\s/.test(ch)) { i++; continue; }
      if (isIdentChar(ch)) {                     // type / element selector
        c++;
        i = skipIdent(sel, i);
        continue;
      }
      i++;
    }
    return [a, b, c];
  }

  function cmpSpec(x, y) {
    if (x[0] !== y[0]) { return x[0] < y[0] ? -1 : 1; }
    if (x[1] !== y[1]) { return x[1] < y[1] ? -1 : 1; }
    if (x[2] !== y[2]) { return x[2] < y[2] ? -1 : 1; }
    return 0;
  }

  // ── collect every colour-declaring rule that is currently in the cascade ──
  var candidates = [], order = 0, unreadableSheets = 0, badSelectors = 0;

  function groupApplies(rule) {
    // A grouping rule whose condition does not hold right now contributes
    // nothing to the cascade, and counting its rules would invent losers that
    // never ran. @layer and @container carry no condition we can evaluate
    // here, so they are recursed into unconditionally.
    try {
      var head = String(rule.cssText || "").slice(0, 12);
      if (head.indexOf("@media") === 0) {
        var mt = (rule.media && rule.media.mediaText) || rule.conditionText || "";
        return mt ? window.matchMedia(mt).matches : true;
      }
      if (head.indexOf("@supports") === 0) {
        var ct = rule.conditionText || "";
        if (!ct || !window.CSS || !CSS.supports) { return true; }
        return CSS.supports(ct);
      }
    } catch (e) { return true; }
    return true;                                 // @layer, @container, unknown
  }

  function walk(rules, sheetIndex, href) {
    for (var i = 0; i < rules.length; i++) {
      var r = rules[i], kids = null;
      try { kids = r.cssRules; } catch (e) { kids = null; }
      // @keyframes is NOT a grouping rule in the cascade sense: its children
      // are keyframe selectors ("0%", "to"), not element selectors, and
      // `el.matches("0%")` throws. Four of them ship in `shared/ks3.css`.
      if (r.keyText !== undefined) { continue; }
      if (String(r.cssText || "").indexOf("@keyframes") === 0 ||
          String(r.cssText || "").indexOf("@-webkit-keyframes") === 0) {
        continue;
      }
      if (r.selectorText && r.style) {
        var v = "";
        try { v = r.style.getPropertyValue("color"); } catch (e) { v = ""; }
        if (v) {
          var pri = "";
          try { pri = r.style.getPropertyPriority("color"); } catch (e) { pri = ""; }
          var list = splitList(r.selectorText);
          for (var s = 0; s < list.length; s++) {
            candidates.push({
              sel: list[s],
              value: v,
              important: pri === "important",
              order: order++,
              sheet: sheetIndex,
              href: href,
              spec: specificity(list[s])
            });
          }
        } else {
          order++;
        }
      } else if (kids && kids.length) {
        if (groupApplies(r)) { walk(kids, sheetIndex, href); }
      }
    }
  }

  for (var s = 0; s < document.styleSheets.length; s++) {
    var sheet = document.styleSheets[s], rules = null;
    try { rules = sheet.cssRules; } catch (e) { unreadableSheets++; continue; }
    if (!rules) { continue; }
    walk(rules, s, sheet.href || "(inline <style>)");
  }

  // ── judge every element on an ink-dark ground ─────────────────────────
  function classesOf(el) {
    var cls = (el.className && el.className.baseVal !== undefined)
      ? el.className.baseVal : (el.className || "");
    return String(cls).trim() ? String(cls).trim().split(/\s+/) : [];
  }

  function describe(el) {
    var c = classesOf(el);
    return el.tagName.toLowerCase() + (c.length ? "." + c.join(".") : "");
  }

  // Is this compound a BARE TYPE selector — `p`, `h2`, `li` — with nothing
  // else attached? That is what makes a rule GENERIC: it claims every element
  // of that tag on the dark ground, regardless of what component it belongs to.
  function isBareType(compound) {
    return /^[A-Za-z][A-Za-z0-9-]*$/.test(compound);
  }

  // Does this compound hang on a `.ks3-*` class the element actually carries?
  // That is what makes a rule the COMPONENT AUTHOR'S: they named this thing.
  function ownedKs3Class(compound, own) {
    var i = 0, found = null;
    while (i < compound.length) {
      var ch = compound[i];
      if (ch === "\\") { i += 2; continue; }
      if (ch === '"' || ch === "'") { i = skipString(compound, i); continue; }
      if (ch === "(") { i = skipBalanced(compound, i, "(", ")"); continue; }
      if (ch === "[") { i = skipBalanced(compound, i, "[", "]"); continue; }
      if (ch === ".") {
        var j = skipIdent(compound, i + 1);
        var name = compound.slice(i + 1, j);
        if (name.indexOf("ks3-") === 0 && own.indexOf(name) >= 0) { found = name; }
        i = j;
        continue;
      }
      i++;
    }
    return found;
  }

  var out = [], checked = 0, withRules = 0, skippedInline = 0;
  var all = document.querySelectorAll("*");

  for (var e = 0; e < all.length; e++) {
    var el = all[e];
    if (!el.closest) { continue; }
    if (!el.closest(".ks3-dark")) { continue; }

    // Rule 7: an inline `color` is explicit author intent and outranks every
    // rule considered here. Nothing to say about it.
    var inlineColor = "";
    try { inlineColor = el.style.getPropertyValue("color"); } catch (x) { inlineColor = ""; }
    if (inlineColor) { skippedInline++; continue; }

    checked++;

    var matched = [];
    for (var ci = 0; ci < candidates.length; ci++) {
      var cand = candidates[ci];
      try {
        if (el.matches(cand.sel)) { matched.push(cand); }
      } catch (x) {
        badSelectors++;                          // unsupported — skip, never crash
      }
    }
    if (!matched.length) { continue; }
    withRules++;

    // Cascade winner: !important tier first, then (a,b,c), then source order.
    var winner = matched[0];
    for (var mi = 1; mi < matched.length; mi++) {
      var m = matched[mi];
      if (m.important !== winner.important) {
        if (m.important) { winner = m; }
        continue;
      }
      var c2 = cmpSpec(m.spec, winner.spec);
      if (c2 > 0 || (c2 === 0 && m.order > winner.order)) { winner = m; }
    }

    if (!isBareType(rightmost(winner.sel))) { continue; }

    var own = classesOf(el), losers = [];
    for (var li = 0; li < matched.length; li++) {
      if (matched[li] === winner) { continue; }
      var owned = ownedKs3Class(rightmost(matched[li].sel), own);
      if (owned) { losers.push(matched[li]); }
    }
    if (!losers.length) { continue; }

    var resolved = getComputedStyle(el).color;
    var lost = [];
    for (var lj = 0; lj < losers.length; lj++) {
      lost.push("`" + losers[lj].sel + "` {color:" + losers[lj].value.trim() +
                "} (" + losers[lj].spec.join(",") + ")");
    }
    out.push(describe(el) +
             " — `" + winner.sel + "` (" + winner.spec.join(",") +
             ") wins with color:" + winner.value.trim() +
             " → resolved " + resolved +
             "; the component's own rule LOST: " + lost.join(", "));
  }

  return { problems: out, checked: checked, withRules: withRules,
           colourRules: candidates.length, skippedInline: skippedInline,
           badSelectors: badSelectors, unreadableSheets: unreadableSheets };
})()
"""


def check_dark_text_specificity(page):
    """⊕ GATE A — a component's own colour must not lose to `.ks3-dark p`.

    Ten times now, an instrument's text class has been written bare at (0,1,0)
    on an ink-dark block, where `.ks3-dark p` is (0,1,1) and takes it. The text
    ships present, correct and invisible; nothing fails, because nothing is
    missing. Every previous fix scoped one instance — this one asks the browser
    which rule actually won, on every element on every ink-dark ground, so the
    eleventh cannot ship.

    Asserted on the UNDRIVEN load: no click has changed a class yet, so the
    cascade being measured is the one a student meets first.

    Returns (problems, info). Read-only — safe on the pass-1 page.
    """
    info = page.eval(_JS_DARK_TEXT_SPECIFICITY)
    return (["DARK-TEXT: " + p for p in info["problems"]], info)


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
    """Composite a background stack (innermost first) into one opaque colour.

    ⊕ MRB-257 — the stack is now a list of `{"bg": ..., "op": ...}` and the
    `opacity` matters. CSS paints an element with `opacity < 1` by rendering
    its subtree into a group and compositing the GROUP, so every background
    inside that element is multiplied by it — and by every dimmed ancestor
    above it. Walking outermost-inwards is what makes that expressible: at each
    level the effective alpha is the background's own alpha times the opacity
    of that level AND everything outside it.

    The old version read background colours only and would have reported the
    grounds under audit 3.5's four instruments at full strength, on rows that
    paint at 45% — which is the "read it from the source" error the audit
    exists to catch, committed by the gate meant to catch it.
    """
    if not stack:
        return None
    ops = [float(n.get("op") or 1) for n in stack]
    ground = (255, 255, 255)
    for k in range(len(stack) - 1, -1, -1):
        bg = parse_rgba(stack[k].get("bg"))
        if not bg or bg[1] <= 0:
            continue
        eff = bg[1]
        for j in range(k, len(stack)):
            eff *= ops[j]
        ground = over((bg[0], eff), ground)
    return ground


def _awaiting_pages(ks3_root):
    """Registered pages that the built tree does not have yet.

    ⊕ MRB-250. A parity row can only be written against a page, and on a unit
    where the engine pass and the authoring passes are separate runs there is a
    window where the components exist and the lesson records do not. B8 spent
    that window writing no rows at all: five instruments shipped with twelve
    assertions between them, the kinds gate stayed green throughout, and a
    dispatch entry read as coverage.

    So the rows are written FIRST, against the page paths the authoring passes
    will produce, and this reports the wait rather than hiding it. Three
    properties, and the third is the one that makes it safe:

    1. A page not in the tree is skipped, so the browser layer does not try to
       load a 404 and report a hundred style failures in Times New Roman.
    2. The skip is COUNTED AND NAMED — `check_structure` prints it and
       `verify_ks3.py` shows it. A skipped assertion must never read as a
       passed one, which is this file's own doctrine.
    3. It self-clears. The moment the page lands, every row on it measures.
       There is no flag to remember to remove, which is the failure mode a
       `parked=` marker would have reintroduced one level up.

    The list of names a page may legitimately be waiting on is bounded by
    `_B9_SLUGS`, which comes from Design's delivered pages via
    `docs/ks3/rail-manifest.md`. A path outside it that does not exist is a
    typo, and a typo would otherwise buy permanent silence.
    """
    out = []
    for rel in _registered_pages():
        path = os.path.join(ks3_root, rel)
        if not os.path.isfile(path):
            out.append(rel)
            continue
        # ⚠️ A COMING-SOON SLOT IS NOT A PAGE, and it is the state B9 is in
        # right now: `build_ks3.py` emits a placeholder for all 183 lesson
        # slots, so the FILE exists from the day the slug is in
        # `structure.py`. Testing existence alone would have loaded six
        # placeholders and reported every B9 row as a vanished component —
        # a hundred and eighty failures describing work that has not started.
        with open(path, encoding="utf-8") as fh:
            if "ks3-coming-soon" in fh.read():
                out.append(rel)
    return out


def _registered_pages():
    seen = []
    for spec in COMPONENTS + CONTRAST:
        if spec["on"] not in seen:
            seen.append(spec["on"])
    return seen


def _pages_needed(ks3_root):
    """Every registered page that the browser layer can actually load.

    ⚠️ NOT filtered by `parked`. A parked spec sits on a page other live specs
    are measured on; dropping the page would drop them too. It is filtered by
    EXISTENCE, which is a different question — see `_awaiting_pages`.
    """
    waiting = set(_awaiting_pages(ks3_root))
    return [rel for rel in _registered_pages() if rel not in waiting]


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


# ── MRB-229 · the 390px reflow gate ──────────────────────────────────────
#
# Three pages, one assertion: `document.scrollWidth === document.clientWidth`.
# Every KS3 page scrolled sideways on a 390px phone until this run — B1 pushed
# the document to 483px, B2 to 572, b9-04 to 577 — and the cause was the header
# trail on all 294 of them. Rainford's students arrive in September and most
# meet the platform on a phone; a page that scrolls sideways on open reads as
# broken before a word of science is read.
#
# ⚠️⚠️ THE VIEWPORT MUST COME FROM `Emulation.setDeviceMetricsOverride`, WHICH
# IS WHAT `page.set_viewport()` SENDS. This is stated in the ticket, in
# ks3_browser.py's header and in the note beside `check_range_binding`, and it
# is the single most likely way to ship a fake pass here: shrinking a container
# does not fire a `max-width` media query — the viewport is still wide — so a
# probe that resizes an element instead measures a layout the truncation rule
# never applied to, and passes silently over the broken one. Headless Chrome
# also FLOORS `--window-size` at about 500px, so a `--window-size=390` run
# would report a 500px layout and find nothing.
#
# One page of each kind, because they are three different header components:
# a lesson carries `<ol class="ks3-trail">`, a unit index and the hub carry
# `<nav class="ks3-crumbs">`, and the truncation rule has to hold for both.
# The lesson is b9-04, which carries the longest trail in Biology and was the
# worst measured page in the key stage.
_REFLOW_PAGES = (
    (B9_SHELF, "lesson · the longest trail in Biology"),
    (_B9_UNIT + "index.html", "unit index"),
    (LANDING, "browse hub"),
)


def check_reflow(browser_mod, url_for, rel, label, width=390):
    """Returns a list of problems. One page, one viewport, measured."""
    problems = []
    with browser_mod.Browser() as b:
        page = b.page(url_for(rel))
        page.set_viewport(width, 844)
        got = page.eval(
            "(function(){var d=document.documentElement;"
            " var t=document.querySelector('.ks3-trail,.ks3-crumbs');"
            " var wide=[];var all=document.querySelectorAll('*');"
            " for(var i=0;i<all.length && wide.length<4;i++){"
            "   var e=all[i];"
            "   if(e.closest('.ks3-figure-scroll')){continue;}"
            "   var r=e.getBoundingClientRect();"
            "   if(r.width>0 && r.right>d.clientWidth+0.5){"
            "     wide.push((e.tagName+'.'+(typeof e.className==='string'?e.className:''))"
            "       .slice(0,52)+' right='+r.right.toFixed(1));}}"
            # A box can sit inside the viewport and still push the document
            # out, because its own CONTENT overflows it — a `nowrap` crumb in
            # a shrunk flex item does exactly that, and a rect-only walk finds
            # nothing to name. Asked as a second question rather than folded
            # into the first, so the message says which kind it is.
            " if(!wide.length){for(var k=0;k<all.length && wide.length<4;k++){"
            "   var x=all[k];"
            "   if(x.closest('.ks3-figure-scroll')){continue;}"
            "   if(x.clientWidth>0 && x.scrollWidth>x.clientWidth+0.5){"
            "     wide.push('content overflows '"
            "       +(x.tagName+'.'+(typeof x.className==='string'?x.className:'')).slice(0,44)"
            "       +' scrollWidth='+x.scrollWidth+' clientWidth='+x.clientWidth);}}}"
            " return {sw:d.scrollWidth, cw:d.clientWidth, iw:window.innerWidth,"
            "         nav:(document.querySelector('header.ks3-nav')||{getBoundingClientRect:"
            "              function(){return{height:-1};}}).getBoundingClientRect().height,"
            r"         crumbs: t ? t.textContent.replace(/\s+/g,' ').trim() : null,"
            "         shown: t ? [].slice.call(t.children).filter(function(c){"
            "              return getComputedStyle(c).display !== 'none';}).length : -1,"
            "         wide: wide};})()")
    # The override itself is asserted. A run where `innerWidth` came back at
    # Chrome's ~500px floor would "pass" this gate on every page while proving
    # nothing at all about a phone.
    if got["iw"] != width:
        problems.append(
            "REFLOW: the device-metrics override did not take on /%s — asked "
            "for %dpx and innerWidth is %s. Every number below would be "
            "measured at the wrong viewport, so none of them is reported."
            % (rel, width, got["iw"]))
        return problems
    if got["sw"] > got["cw"]:
        problems.append(
            "REFLOW: /%s (%s) scrolls sideways at %dpx — scrollWidth %s vs "
            "clientWidth %s. Overflowing: %s"
            % (rel, label, width, got["sw"], got["cw"],
               "; ".join(got["wide"]) or "nothing found by either walk, so "
               "the overflow is a margin, a pseudo-element or a shadow"))
    # The truncation itself, not only its consequence. A page could stop
    # overflowing because someone shrank the type, and this gate would smile.
    if got["shown"] > 3:
        problems.append(
            "REFLOW: /%s (%s) shows %d crumb elements at %dpx — MRB-229 rules "
            "unit and page only, which is three: the crumb, its separator and "
            "the current page. Reading: %r"
            % (rel, label, got["shown"], width, got["crumbs"]))
    return problems


def check_figure_cue(browser_mod, url_for, rel):
    """Audit 3.9 — the edge fade is on when the figure is scrollable, off when
    it is not. Both ends, because a mask that is always on is not a cue."""
    problems = []
    JS = ("(function(){var f=document.querySelector('.ks3-figure-scroll');"
          " if(!f){return null;}var cs=getComputedStyle(f);"
          " return {cw:f.clientWidth, sw:f.scrollWidth,"
          "         mask:(cs.maskImage||cs.webkitMaskImage||'none')};})()")
    with browser_mod.Browser() as b:
        page = b.page(url_for(rel))
        page.set_viewport(390, 844)
        narrow = page.eval(JS)
        page.set_viewport(1440, 900)
        wide = page.eval(JS)
    if narrow is None or wide is None:
        problems.append(
            "FIGURE CUE: /%s renders no `.ks3-figure-scroll`, so audit 3.9's "
            "assertion did not run. It is registered on this page because this "
            "page carries the two-panel moth figure." % rel)
        return problems
    if not (narrow["sw"] > narrow["cw"]):
        problems.append(
            "FIGURE CUE: /%s does not overflow at 390px (%s in %s), so the "
            "premise of audit 3.9 has changed and the fade needs re-thinking "
            "rather than keeping." % (rel, narrow["sw"], narrow["cw"]))
    elif narrow["mask"] == "none":
        problems.append(
            "FIGURE CUE: /%s hides %d of %dpx of the figure at 390px and draws "
            "NO edge fade. The visible window ends exactly at the panel "
            "boundary, so it reads as a complete diagram — while the caption "
            "under it talks about the panel on the right."
            % (rel, narrow["sw"] - narrow["cw"], narrow["sw"]))
    if wide["sw"] <= wide["cw"] and wide["mask"] != "none":
        problems.append(
            "FIGURE CUE: /%s draws the edge fade at 1440px, where the figure "
            "fits (%s in %s). A fade that is always there says nothing; the "
            "threshold has detached from the condition it stands for."
            % (rel, wide["sw"], wide["cw"]))
    return problems


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
            # ⊕ MRB-257 — the FOREGROUND is dimmed by the same ancestors the
            # ground is. Reading `color` and stopping there is how a 2.48:1 row
            # measures 6.08:1 and passes.
            #
            # ⚠️ AND IT COMPOSITES OVER THE BACKDROP BEHIND ITS OWN ELEMENT,
            # NOT OVER THE ELEMENT'S PAINTED BACKGROUND. This is the one place
            # the naive model is wrong in a way that matters. CSS renders an
            # element with `opacity` by drawing its subtree into a group — the
            # background first, the glyphs over it — and compositing the whole
            # GROUP once. Inside the group the glyph REPLACES the background,
            # so the glyph and the background each land on the same backdrop
            # and neither lands on the other. Compositing the glyph over the
            # already-composited background applies the opacity twice and
            # reports a locked control at 3.02:1 that a browser paints at
            # 4.86:1 — a number that is wrong in the safe direction today and
            # would be wrong in the unsafe one the moment a light glyph sat on
            # a dark dimmed fill.
            fg_op = page.eval("window.__ks3.opacityChain(%r)" % fg_sel)
            fg_stack = page.eval("window.__ks3.groundStack(%r)" % fg_sel)
            backdrop = _flatten(fg_stack[1:]) if fg_stack else bg
            fg_rgba = parse_rgba(fg)
            g = bg
            if fg_rgba is not None and backdrop is not None:
                a = fg_rgba[1] * (fg_op if fg_op is not None else 1.0)
                f = over((fg_rgba[0], a), backdrop) if a < 0.999 else fg_rgba[0]
            else:
                f = parse_rgb(fg)
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

    n_hidden_checked = 0
    hidden_problems = []
    n_dark_checked = 0
    dark_problems = []
    server, port = browser_mod.serve(served_root)
    try:
        # ⊕ MRB-242 — a FRESH Chrome PER PAGE, which is what the build contract
        # §6 has said all along and what this loop was not doing. One browser
        # held open across every page accumulates the KS3 canvas rAF loops (they
        # keep running after the driver moves on) until the DevTools socket
        # degrades around the twelfth page; from there `__ks3.q()` starts
        # answering null for selectors that are demonstrably in the DOM. That is
        # not a slow gate, it is a gate whose result depends on how many pages
        # ran before it — it reported all six of c2-02's components "registered
        # but not rendered" while the page rendered them perfectly in isolation.
        # It passed at HEAD by luck, and one extra per-page read tipped it over.
        for rel in _pages_needed(ks3_root):
            url = "http://127.0.0.1:%d/%s/%s" % (port, prefix, rel)
            with browser_mod.Browser() as b:

                # ── pass 1: the page as the generator wrote it ──
                page = fresh(b, url, rel)
                if page is None:
                    continue
                drain_console(page, rel, "")
                # ⊕ MRB-242 — on the UNDRIVEN load, before anything is clicked,
                # so "hidden means hidden" is an unambiguous claim. Free: this
                # page is already open, and the audit only reads.
                hid, hidinfo = check_hidden_stays_hidden(page)
                # ⚠️ Kept OUT of `problems`. verify_ks3.py reads that list as
                # "a registered component is no longer rendered" and would
                # report these six as six vanished components, which is a
                # different defect on a different page. They are returned in
                # their own channel and get their own check.
                hidden_problems.extend("/%s — %s" % (rel, h) for h in hid)
                n_hidden_checked += hidinfo["checked"]
                # ⊕ GATE A — same undriven load, same reasoning, its own
                # channel. A component whose colour lost to `.ks3-dark p` is
                # not a vanished component and must not be reported as one.
                drk, drkinfo = check_dark_text_specificity(page)
                dark_problems.extend("/%s — %s" % (rel, d) for d in drk)
                n_dark_checked += drkinfo["checked"]
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
                    # ⊕ MRB-245 — A DRIVE THAT THROWS IS A FAILURE, NOT A
                    # CRASH, and this `try` is the difference between one red
                    # gate and a total blackout of every browser-asserted gate
                    # in the key stage.
                    #
                    # The branch below has always handled a drive that RETURNS
                    # an error string. A drive that throws — one undeclared
                    # variable is enough — raises `JSError` out of `page.eval`,
                    # and that propagated straight out of this function: the
                    # loop stopped where it stood, and GATE A, the MRB-242
                    # hidden-element audit and all 56 contrast pairs never ran
                    # at all. `verify_ks3.py` exits 1 either way, so **a total
                    # outage of the browser layer was indistinguishable from
                    # one honest red gate**. That is the exact class of defect
                    # this ticket exists to close: a gate that has stopped
                    # enforcing and does not say so. Found by a typo in a B7
                    # drive, which is the cheapest way it will ever be found.
                    #
                    # So: the throw becomes a `problems.append` like any other
                    # — the build still goes red — and every other drive and
                    # every other page still runs. A broken drive costs its own
                    # assertions and nobody else's, and the message says
                    # plainly that they did not run, because a SKIPPED
                    # assertion must never be able to read as a passed one.
                    try:
                        err = page.eval(DRIVES[drive])
                    except browser_mod.JSError as exc:
                        err = ("the drive itself threw, so it never reached "
                               "the state it was written to measure: %s" % exc)
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
        # ── MRB-229 · zero horizontal overflow at a true 390px ──
        # Its own loop and its own fresh browser per page, because it changes
        # the viewport and every measurement above assumes the default one.
        def _url(rel):
            return "http://127.0.0.1:%d/%s/%s" % (port, prefix, rel)

        reflow_problems = []
        for rel, label in _REFLOW_PAGES:
            if not os.path.exists(os.path.join(ks3_root, rel)):
                reflow_problems.append(
                    "REFLOW: /%s (%s) is not in the built tree, so MRB-229's "
                    "assertion did not run on it." % (rel, label))
                continue
            reflow_problems.extend(
                check_reflow(browser_mod, _url, rel, label))
        problems.extend(reflow_problems)
        style_rows.append(
            ("⊕ MRB-229 · no horizontal overflow at 390px (device metrics)",
             "document.scrollWidth == clientWidth, on a lesson, a unit index "
             "and the hub",
             "0 problems across %d page(s)" % len(_REFLOW_PAGES),
             "%d problem(s)" % len(reflow_problems),
             not reflow_problems))

        # ── audit 3.9 · the figure's edge cue, asserted at both ends ──
        cue_problems = []
        if os.path.exists(os.path.join(ks3_root, B11_SEL)):
            cue_problems = check_figure_cue(browser_mod, _url, B11_SEL)
        problems.extend(cue_problems)
        style_rows.append(
            ("⊕ audit 3.9 · the moth figure says it continues",
             "edge fade present at 390px, absent at 1440px",
             "0 problems", "%d problem(s)" % len(cue_problems),
             not cue_problems))
    finally:
        server.shutdown()

    return (problems, style_rows, contrast_rows,
            (hidden_problems, n_hidden_checked),
            (dark_problems, n_dark_checked))
